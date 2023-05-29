import logging
import os

from helpers import FileHandler, FileObject, UpdateFile

logging.basicConfig(
    level=logging.INFO, format="%(levelname)s: %(asctime)s | %(message)s"
)
LOG = logging.getLogger("build")
WORK_DIR = os.getenv("WORK_DIR", os.getcwd())
TOKEN = os.getenv("GH_TOKEN")
ORG = "jmgreg31"
REPO = "terraform-aws-cloudfront"


class UpdateReadme(UpdateFile):
    def get_path(self) -> str:
        return f"{WORK_DIR}/README.md"

    def get_search(self) -> str:
        return r"v\d+\.\d+\.\d+"

    def get_sub(self) -> str:
        return self.version


class UpdateChangeLog(UpdateFile):
    def get_path(self) -> str:
        return f"{WORK_DIR}/CHANGELOG.md"

    def get_search(self) -> str:
        return r"UNRELEASED"

    def get_sub(self) -> str:
        return self.version


class UpdateExampleTerraform(UpdateFile):
    def get_path(self) -> str:
        return f"{WORK_DIR}/example/main.tf"

    def get_search(self) -> str:
        return r"source[ \t]+\=.*"

    def get_sub(self) -> str:
        return f'source = "git::https://github.com/{ORG}/{REPO}.git?ref={self.version}"'


class BumpHandler(FileHandler):
    def get_file_changes(self) -> list[FileObject]:
        file_changes = []
        file_changes.append(UpdateReadme(self.version).object)
        file_changes.append(UpdateChangeLog(self.version).object)
        file_changes.append(UpdateExampleTerraform(self.version).object)
        return file_changes

    def push_file_changes(self) -> None:
        with os.chdir(WORK_DIR):
            os.system("terraform fmt example/ > /dev/null 2>&1")
            os.system('git config --global user.email "jmgreg31@gmail.com"')
            os.system('git config --global user.name "Jon Greg"')
            os.system("git config --global init.defaultBranch master")
            os.system(f"git init")
            os.system(
                f"git remote add origin https://jmgreg31:{TOKEN}@github.com/{ORG}/{REPO}.git > /dev/null 2>&1"
            )
            # os.system("git checkout master")
            os.system("git add README.md")
            os.system("git add CHANGELOG.md")
            os.system("git add example/main.tf")
            os.system("git add example/terraform.tfvars")
            os.system(f'git commit -m "(ci): Bump Version to {self.version}"')
            if not self.dry_run:
                os.system("git push origin master")
            else:
                LOG.info(f"Version {self.version} is the latest release")

            # os.system(f"{WORK_DIR}/terraform fmt {WORK_DIR}/example/ > /dev/null 2>&1")
            # os.system('git config --global user.email "jmgreg31@gmail.com"')
            # os.system('git config --global user.name "Jon Greg"')
            # os.system("git config --global init.defaultBranch master")
            # os.system(f"cd {WORK_DIR} && git init")
            # os.system(
            #     f"cd {WORK_DIR} && git remote add origin https://jmgreg31:{TOKEN}@github.com/{ORG}/{REPO}.git > /dev/null 2>&1"
            # )
            # # os.system("git checkout master")
            # os.system(f"cd {WORK_DIR} && git add README.md")
            # os.system(f"cd {WORK_DIR} && git add CHANGELOG.md")
            # os.system(f"cd {WORK_DIR} && git add example/main.tf")
            # os.system(f"cd {WORK_DIR} && git add example/terraform.tfvars")
            # os.system(
            #     f'cd {WORK_DIR} && git commit -m "(ci): Bump Version to {self.version}"'
            # )
            # if not self.dry_run:
            #     os.system(f"cd {WORK_DIR} && git push origin master")
            # else:
            #     LOG.info(f"Version {self.version} is the latest release")


def main():
    BumpHandler().main_handler()


if __name__ == "__main__":
    main()

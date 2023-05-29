import os

from helpers import FileHandler, FileObject, UpdateFile

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
        os.system(f"{WORK_DIR}/terraform fmt {WORK_DIR}/example/")
        os.system('git config --global user.email "jmgreg31@gmail.com"')
        os.system('git config --global user.name "Jon Greg"')
        os.system("git checkout master")
        os.system(f"git add {WORK_DIR}/README.md")
        os.system(f"git add {WORK_DIR}/CHANGELOG.md")
        os.system(f"git add {WORK_DIR}/example/main.tf")
        os.system(f"git add {WORK_DIR}/example/terraform.tfvars")
        os.system(f'git commit -m "(ci): Bump Version to {self.version}"')
        os.system(
            f"git remote set-url origin https://jmgreg31:{TOKEN}@github.com/{ORG}/{REPO}.git > /dev/null 2>&1"
        )
        if not self.dry_run:
            os.system("git push origin master")
        else:
            print(f"Version {self.version} is the latest release")


def main():
    BumpHandler().main_handler()


if __name__ == "__main__":
    main()
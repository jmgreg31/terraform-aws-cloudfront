# pylint: disable = wrong-import-position
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from scripts.helpers import FileContext, FileHandler, FileObject, UpdateFile
from scripts.logger import CustomLogger

LOG = CustomLogger("build")
TOKEN = os.getenv("GH_TOKEN")
ORG = "jmgreg31"
REPO = "terraform-aws-cloudfront"


class UpdateReadme(UpdateFile):
    def get_path(self) -> str:
        return "README.md"

    def get_search(self) -> str:
        return r"v\d+\.\d+\.\d+"

    def get_sub(self) -> str:
        return self.version


class UpdateChangeLog(UpdateFile):
    def get_path(self) -> str:
        return "CHANGELOG.md"

    def get_search(self) -> str:
        return r"UNRELEASED"

    def get_sub(self) -> str:
        return self.version


class UpdateExampleTerraform(UpdateFile):
    def get_path(self) -> str:
        return "example/main.tf"

    def get_search(self) -> str:
        return r"source[ \t]+\=.*"

    def get_sub(self) -> str:
        return f'source = "git::https://github.com/{ORG}/{REPO}//cloudfront?ref={self.version}"'


class BumpHandler(FileHandler):
    def get_file_changes(self) -> list[FileObject]:
        file_changes = []
        file_changes.append(UpdateReadme(self.version).object)
        file_changes.append(UpdateChangeLog(self.version).object)
        file_changes.append(UpdateExampleTerraform(self.version).object)
        return file_changes

    def push_file_changes(self) -> None:
        with FileContext("."):
            os.system("terraform fmt example/ > /dev/null 2>&1")
            os.system('git config --global user.email "jmgreg31@gmail.com"')
            os.system('git config --global user.name "Jon Greg"')
            os.system("git config --global init.defaultBranch master")
            os.system("git init")
            os.system(
                f"git remote add origin https://jmgreg31:{TOKEN}@github.com/{ORG}/{REPO}.git > /dev/null 2>&1"
            )
            os.system("git fetch origin")
            os.system("git add README.md")
            os.system("git add CHANGELOG.md")
            os.system("git add example/main.tf")
            os.system("git add example/terraform.tfvars")
            os.system(f'git commit -m "(ci): Bump Version to {self.version}"')
            if not self.dry_run:
                os.system("git push origin master")
            else:
                LOG.info(f"Version {self.version} is the latest release")


def main():
    BumpHandler().main_handler()


if __name__ == "__main__":
    main()

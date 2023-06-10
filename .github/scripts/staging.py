# pylint: disable = wrong-import-position
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from scripts.helpers import FileHandler, FileObject, UpdateFile
from scripts.logger import CustomLogger

LOG = CustomLogger("staging")


class UpdateExampleTerraform(UpdateFile):
    def get_path(self) -> str:
        return "example/main.tf"

    def get_search(self) -> str:
        return r"source[ \t]+\=.*"

    def get_sub(self) -> str:
        return 'source = "../cloudfront/"'


class StagingHandler(FileHandler):
    def get_file_changes(self) -> list[FileObject]:
        file_changes = []
        file_changes.append(UpdateExampleTerraform(self.version).object)
        return file_changes

    def push_file_changes(self) -> None:
        LOG.info("No files to push for Staging Workflow")


def main():
    StagingHandler().main_handler()


if __name__ == "__main__":
    main()

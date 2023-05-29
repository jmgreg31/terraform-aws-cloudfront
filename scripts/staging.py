import os

from helpers import FileHandler, FileObject, UpdateFile

WORK_DIR = os.getenv("WORK_DIR")


class UpdateExampleTerraform(UpdateFile):
    def get_path(self) -> str:
        return f"{WORK_DIR}/example/main.tf"

    def get_search(self) -> str:
        return r"source[ \t]+\=.*"

    def get_sub(self) -> str:
        return 'source = "../"'


class StagingHandler(FileHandler):
    def get_file_changes(self) -> list[FileObject]:
        file_changes = []
        file_changes.append(UpdateExampleTerraform(self.version).object)
        return file_changes

    def push_file_changes(self) -> None:
        print("No files to push for Staging Workflow")


def main():
    StagingHandler().main_handler()


if __name__ == "__main__":
    main()

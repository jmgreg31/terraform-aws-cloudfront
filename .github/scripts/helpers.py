import logging
import os
import re
import traceback
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO, format="%(levelname)s: %(asctime)s | %(message)s"
)
LOG = logging.getLogger("helpers")
WORK_DIR = os.getenv("WORK_DIR", os.getcwd())
TOKEN = os.getenv("GH_TOKEN")
ORG = "jmgreg31"
REPO = "terraform-aws-cloudfront"


class GitHubClient:
    def __init__(self) -> None:
        self.base_url = "https://api.github.com"

    def _get_headers(self) -> dict:
        return {
            f"Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_latest_release(self) -> str:
        url = f"{self.base_url}/repos/{ORG}/{REPO}/releases/latest"
        response = requests.get(url, headers=self._get_headers())
        latest_version = response.json()["tag_name"]
        LOG.info(f"Latest Version: {latest_version}")
        return latest_version


@dataclass
class FileObject:
    file_path: str
    search: str
    sub: str


class UpdateFile(ABC):
    def __init__(self, version: str) -> None:
        self.version = version
        self.path = self.get_path()
        self.search = self.get_search()
        self.sub = self.get_sub()

    @abstractmethod
    def get_path(self) -> str:
        """The full path to the file"""

    @abstractmethod
    def get_search(self) -> str:
        """The regex search expression"""

    @abstractmethod
    def get_sub(self) -> str:
        """The string that should be substitued"""

    @property
    def object(self) -> FileObject:
        return FileObject(self.path, self.search, self.sub)


class FileHandler(ABC):
    def __init__(self) -> None:
        self.version = self.get_version()
        self.latest_version = GitHubClient().get_latest_release()

    @property
    def dry_run(self) -> bool:
        return self.version == self.latest_version

    @staticmethod
    def update_file(file_object: FileObject) -> None:
        with open(file_object.file_path, "r") as read_file:
            current_content = read_file.read()
            new_content = re.sub(file_object.search, file_object.sub, current_content)
        with open(file_object.file_path, "w") as write_file:
            write_file.write(new_content)

    def get_version(self) -> str:
        with open(f"{WORK_DIR}/VERSION", "r") as version:
            for line in version:
                output = line
                bumpversion = f"v{output}"
        proposed_version = bumpversion.rstrip()
        LOG.info(f"Proposed Version: {proposed_version}")
        return proposed_version

    @abstractmethod
    def get_file_changes(self) -> list[FileObject]:
        """Return a list of FileObjects to Change"""

    @abstractmethod
    def push_file_changes(self) -> None:
        """Provide Logic to push any changes"""

    def main_handler(self) -> None:
        file_list = self.get_file_changes()
        for file in file_list:
            self.update_file(file)
        self.push_file_changes()


class FileContext:
    def __init__(self, path: str):
        self.path = path
        self.origin = Path().absolute()

    def __enter__(self):
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            LOG.info(traceback.format_exception(exc_type, exc_value, tb))
        os.chdir(self.origin)

import os
import re

import requests

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
        return response.json()["tag_name"]


def get_version() -> str:
    with open(f"{WORK_DIR}/VERSION", "r") as version:
        for line in version:
            output = line
            bumpversion = "v" + output
    return bumpversion.rstrip()


def update_file(path: str, expression: str, replacement: str) -> None:
    with open(path, "r") as read_file:
        current_content = read_file.read()
        new_content = re.sub(expression, replacement, current_content)
    with open(path, "w") as write_file:
        write_file.write(new_content)


def file_handler(version: str) -> None:
    tf_replace = (
        "source = "
        + '"git::https://github.com/jmgreg31/terraform-aws-cloudfront.git?ref={}"'.format(
            version
        )
    )
    file_list = [
        (f"{WORK_DIR}/README.md", r"v\d+\.\d+\.\d+", version),
        (f"{WORK_DIR}/CHANGELOG.md", r"UNRELEASED", version),
        (f"{WORK_DIR}/example/main.tf", r"source[ \t]+\=.*", tf_replace),
    ]
    for file in file_list:
        update_file(file[0], file[1], file[2])


def push_changes(version: str, dry_run: bool) -> None:
    os.system(f"{WORK_DIR}/terraform fmt {WORK_DIR}/example/")
    os.system(
        'git config --global user.email "jmgreg31@gmail.com" && \
               git config --global user.name "Jon Greg"'
    )
    os.system("git checkout master")
    os.system(
        f"git add {WORK_DIR}/README.md {WORK_DIR}/CHANGELOG.md {WORK_DIR}/example/main.tf {WORK_DIR}/example/terraform.tfvars"
    )
    os.system(f'git commit -m "(ci): Bump Version to {version}"')
    os.system(
        "git remote set-url origin https://jmgreg31:${GH_TOKEN}@github.com/jmgreg31/terraform-aws-cloudfront.git > /dev/null 2>&1"
    )
    if not dry_run:
        os.system("git push origin master")
    else:
        print(f"Version {version} is the latest release")


def main():
    bump_version = get_version()
    latest_version = GitHubClient().get_latest_release()
    dry_run = bump_version == latest_version
    file_handler(bump_version)
    push_changes(bump_version, dry_run)


if __name__ == "__main__":
    main()

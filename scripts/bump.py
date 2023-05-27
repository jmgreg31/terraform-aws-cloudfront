import os
import re

WORK_DIR = os.getenv("WORK_DIR")


def get_version() -> str:
    with open(f"{WORK_DIR}/VERSION", "r") as version:
        for line in version:
            output = line
            bumpversion = "v" + output
    return bumpversion.rstrip()


def get_data(path: str, expression: str, replacement: str) -> str:
    with open(path, "r") as readme:
        data = readme.read()
        data = re.sub(expression, replacement, data)
    return data


def update_readme() -> None:
    bumpversion = get_version()
    data = get_data(f"{WORK_DIR}/README.md", r"v\d+\.\d+\.\d+", bumpversion)
    with open("README.md", "w") as newfile:
        newfile.write(data)


def update_changelog() -> None:
    bumpversion = get_version()
    data = get_data(f"{WORK_DIR}/CHANGELOG.md", r"UNRELEASED", bumpversion)
    with open(f"{WORK_DIR}/CHANGELOG.md", "w") as newfile:
        newfile.write(data)


def update_example() -> None:
    bumpversion = get_version()
    replacement = (
        "source = "
        + '"git::https://github.com/jmgreg31/terraform-aws-cloudfront.git?ref={}"'.format(
            bumpversion
        )
    )
    data = get_data(f"{WORK_DIR}/example/main.tf", r"source[ \t]+\=.*", replacement)
    with open(f"{WORK_DIR}/example/main.tf", "w") as newfile:
        newfile.write(data)
    os.system(f"{WORK_DIR}/terraform fmt {WORK_DIR}/example/")


def push_changes() -> None:
    bumpversion = get_version()
    os.system(
        'git config --global user.email "jmgreg31@gmail.com" && \
               git config --global user.name "Jon Greg"'
    )
    os.system("git checkout master")
    os.system("git add README.md CHANGELOG.md example/main.tf example/terraform.tfvars")
    os.system('git commit -m "(ci): Bump Version to {}"'.format(bumpversion))
    os.system(
        "git remote set-url origin https://jmgreg31:${GH_TOKEN}@github.com/jmgreg31/terraform-aws-cloudfront.git > /dev/null 2>&1"
    )
    os.system("git push origin master")


if __name__ == "__main__":
    update_readme()
    update_changelog()
    update_example()
    push_changes()

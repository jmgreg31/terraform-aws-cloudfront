import os
import re

WORK_DIR = os.getenv("WORK_DIR")


def update_file(path: str, expression: str, replacement: str) -> None:
    with open(path, "r") as readme:
        data = readme.read()
        data = re.sub(expression, replacement, data)
    with open(path, "w") as newfile:
        newfile.write(data)


def update_example() -> None:
    replacement = 'source = "../"'
    update_file(f"{WORK_DIR}/example/main.tf", r"source[ \t]+\=.*", replacement)
    os.system("terraform fmt example/")


if __name__ == "__main__":
    update_example()

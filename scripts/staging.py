import os
import re

WORK_DIR = os.getenv("WORK_DIR")


def update_file(path: str, expression: str, replacement: str) -> None:
    with open(path, "r") as read_file:
        current_content = read_file.read()
        new_content = re.sub(expression, replacement, current_content)
    with open(path, "w") as write_file:
        write_file.write(new_content)


def update_example() -> None:
    replacement = 'source = "../"'
    update_file(f"{WORK_DIR}/example/main.tf", r"source[ \t]+\=.*", replacement)


if __name__ == "__main__":
    update_example()

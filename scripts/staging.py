import os
import re

CWD = os.getcwd()


def update_file(path: str, expression: str, replacement: str) -> None:
    with open(path, "r") as readme:
        data = readme.read()
        data = re.sub(expression, replacement, data)
    with open(path, "w") as newfile:
        newfile.write(data)


def update_example() -> None:
    replacement = "source = ../"
    update_file(f"{CWD}/example/main.tf", r"source[ \t]+\=.*", replacement)
    os.system("./terraform fmt example/")


if __name__ == "__main__":
    update_example()

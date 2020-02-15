import re

with open ('../VERSION','r') as version:
    for line in version:
        bumpversion=line

print(bumpversion)
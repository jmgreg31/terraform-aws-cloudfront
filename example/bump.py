import re

with open ('../VERION','r') as version:
    for line in version:
        bumpversion=line

print(bumpversion)
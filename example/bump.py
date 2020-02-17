import re
import os

def getVersion():
    with open ('../VERSION','r') as version:
        for line in version:
            output=line
            bumpversion='v'+ output
    return bumpversion

def getData(filename,expression,replacement):
    with open (filename, 'r') as readme:
        data=readme.read()
        data=re.sub(expression, replacement, data)
    return data

def updateREADME():
    bumpversion = getVersion()
    data=getData('../README.md',r'v\d+\.\d+\.\d+',bumpversion)
    with open ('../README.md', 'w') as newfile:
        newfile.write(data)

def updateCHANGELOG():
    bumpversion = getVersion()
    data=getData('../CHANGELOG.md',r'UNRELEASED',bumpversion)
    with open ('../CHANGELOG.md', 'w') as newfile:
        newfile.write(data)

def updateMaintf():
    bumpversion = getVersion()
    replacement = "source = " + "\"git::https://github.com/jmgreg31/terraform-aws-cloudfront.git?ref={}\"".format(bumpversion)
    data=getData('main.tf',r'source[ \t]+\=.*',replacement)
    with open ('main.tf', 'w') as newfile:
        newfile.write(data)
    os.system('./terraform fmt')

def updateGit():
    bumpversion = getVersion()
    os.system('git config --global user.email \"travis@travis-ci.org\" && \
               git config --global user.name "Travis CI"')
    os.system('git checkout master')
    os.system('git add ../README.md ../CHANGELOG.md main.tf terraform.tfvars')
    os.system('git commit -m "Bump Version to {} [skip ci]"'.format(bumpversion))
    os.system('git remote set-url origin https://jmgreg31:${GH_TOKEN}@github.com/jmgreg31/terraform-aws-cloudfront.git > /dev/null 2>&1')
    os.system('git push origin master')

if __name__ == '__main__':
    updateREADME()
    updateCHANGELOG()
    updateMaintf()
    updateGit()
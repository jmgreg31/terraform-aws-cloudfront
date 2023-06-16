.PHONY: install lock fmt fmt-py lint coverage coverage-report docs create-docs view-docs pcommit commit test

PWD=$$(pwd)

install:
	@pip3 install pipenv

lock:
	@pipenv lock
	@pipenv sync --dev

fmt:
	# Terraform must be installed locally
	@pipenv run terraform fmt ./

fmt-py:
	@pipenv run black .github/scripts/

lint:
	@pipenv run pylint .github/scripts/

test:
	@pipenv run pytest .github/tests/

coverage:
	@pipenv run pytest --junitxml=junit_xml_test_report.xml --cov .github/scripts/ .github/tests --cov-branch

coverage-report:
	@pipenv run pytest --junitxml=junit_xml_test_report.xml --cov .github/scripts/ .github/tests --cov-branch --cov-report html
	@open file://${PWD}/htmlcov/index.html

docs: create-docs pcommit

create-docs:
	@pipenv run pdoc -o .github/docs/ -d google .github/scripts/

view-docs:
	@open file://${PWD}/.github/docs/index.html

pcommit:
	@pipenv run pre-commit install
	@pipenv run pre-commit run --all-files

commit:
	@pipenv run pre-commit install
	@pipenv run git add --all
	@read -p "Commit Message: " COMMIT_MESSAGE \
	&& pipenv run git commit -m "$${COMMIT_MESSAGE}"
	@read -p "Commit Branch: " COMMIT_BRANCH \
	&& pipenv run git push origin $${COMMIT_BRANCH}

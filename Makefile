VIRTUALENV := python3 -m venv

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## venv - Install the virtual environment
venv:
	$(VIRTUALENV) ~/.venv/tuneuptechnology/
	ln -snf ~/.venv/tuneuptechnology/ venv
	venv/bin/pip install -e ."[dev]"

## install - Install the project locally
install: | venv

## run - Runs the flask server
run:
	venv/bin/python tuneuptechnology/app.py

## clean - Remove the virtual environment and clear out .pyc files
clean:
	rm -rf ~/.venv/tuneuptechnology/ venv
	find . -name '*.pyc' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

## lint - Lint the project
lint:
	venv/bin/flake8 tuneuptechnology/*.py
	venv/bin/flake8 test/unit/*.py

## test - Test the project
test:
	venv/bin/pytest

## coverage - Test the project and generate an HTML coverage report
coverage:
	venv/bin/pytest --cov=tuneuptechnology --cov-branch --cov-report=html --cov-report=term-missing

.PHONY: help install run clean lint test coverage

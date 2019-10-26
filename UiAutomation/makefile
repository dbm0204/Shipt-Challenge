.PHONY: help prepare-dev test lint run doc
VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3
.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "prepare development environment, use only once"
	@echo "make test"
	@echo "run tests"
	@echo "make lint"
	@echo "un pylint and mypy"
	@echo "make run"
	@echo "run project"
	@echo "make doc"
	@echo "build sphinx documentation"

prepare-dev:
	brew install python3.7 python3-pip
	python3 -m pip install virtualenv
	make venv

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
env: 
	$(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: 
	setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .
	touch $(VENV_NAME)/bin/activate
run: 
	${PYTHON} TestRunner.py

clean:	
	find . -name '*.pyc' -delete


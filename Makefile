.PHONY: init install clean run test

VENV_PROMPT = pypomo
APP_ENTRY = pypomodoro/main.py

VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.DEFAULT_GOAL := help

help:
	@echo "Run make <target> with:"
	@echo "  init - creates venv and installs dependencies"
	@echo "  install - installs "
	@echo "  run - runs app "
	@echo "  test - runs tests"

$(VENV)/bin/activate : requirements-dev.txt
	python3 -m venv $(VENV) --prompt=$(VENV_PROMPT)
	$(PIP) install -r requirements-dev.txt

init: $(VENV)/bin/activate

install: clean
	 $(PYTHON) setup.py install

run: $(VENV)/bin/activate
	 $(PYTHON) $(APP_ENTRY)

test: $(VENV)/bin/activate
	$(PYTHON) -m unittest -v

clean: clean-build clean-pyc ## remove all build and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

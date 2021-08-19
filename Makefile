.PHONY: init build run unittest test

VENV_PROMPT = pypomo
APP_ENTRY = pypomodoro/main.py

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.DEFAULT_GOAL := help

help:
	@echo "Run make <target> with:"
	@echo "  init - creates venv and installs dependencies"
	@echo "  run - runs app"
	@echo "  test - runs tests"

init: $(VENV)/bin/activate

run: $(VENV)/bin/activate
	 $(PYTHON) $(APP_ENTRY)

$(VENV)/bin/activate : requirements.txt
	python3 -m venv $(VENV) --prompt=$(VENV_PROMPT)
	$(PIP) install -r requirements.txt

test: $(VENV)/bin/activate
	$(PYTHON) -m unittest -v

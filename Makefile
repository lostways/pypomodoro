.PHONY: init build run unittest test

VENV_PROMPT = pypomo
APP_ENTRY = pypomodoro/main.py

VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.DEFAULT_GOAL := help

help:
	@echo "Run make <target> with:"
	@echo "  init - creates venv and installs dependencies"
	@echo "  run - runs app"
	@echo "  test - runs tests"

$(VENV)/bin/activate : requirements-dev.txt
	python3 -m venv $(VENV) --prompt=$(VENV_PROMPT)
	$(PIP) install -r requirements-dev.txt

init: $(VENV)/bin/activate

run: $(VENV)/bin/activate
	 $(PYTHON) $(APP_ENTRY)

test: $(VENV)/bin/activate
	$(PYTHON) -m unittest -v

clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(VENV)

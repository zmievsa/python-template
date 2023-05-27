SHELL := /bin/bash
py_warn = PYTHONDEVMODE=1

format:
	poetry run ruff . --fix; \
	poetry run black .;

test:
	poetry run pytest -v --cov={{ package_name }} --cov-report=term-missing:skip-covered --cov-branch --cov-report=xml tests;

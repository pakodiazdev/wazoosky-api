.PHONY: format lint types check test test-with-coverage

# Variables
GENERATE_HTML ?= true

format:
	black .
	isort .
	autopep8 --in-place --recursive --aggressive --aggressive .

lint:
	flake8 .

types:
	mypy .

check:
	black --check .
	isort --check-only .
	flake8 .
	mypy .

test:
	python manage.py test

test-with-coverage:
	coverage run --source=. -m pytest && \
	coverage xml -o coverage.xml

start:
	python manage.py runserver 0.0.0.0:8000

.PHONY: format lint types check test test-with-coverage

# Variables
GENERATE_HTML ?= true

format:
	black .
	isort .

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
	coverage run --source='core,config' manage.py test
	coverage xml -o coverage.xml
ifeq ($(GENERATE_HTML),true)
	coverage html -d htmlcov
endif
	coverage report

start:
	python manage.py runserver 0.0.0.0:8000

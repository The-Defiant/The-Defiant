install:
	poetry install

test:
	poetry run pytest

develop:
	poetry run uvicorn defiant.App:app --reload

build:
	poetry build
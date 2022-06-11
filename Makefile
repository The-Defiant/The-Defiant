install:
	poetry install

test:
	poetry run pytest

develop:
	poetry run uvicorn backend.App:app --reload
main: log/ python_starter/.env
	poetry run dev

test:
	poetry run pytest tests/

format:
	poetry run black python_starter/ tests/

type-check:
	poetry run mypy -p python_starter

export:
	poetry export -f requirements.txt --output requirements.txt

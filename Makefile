main: log/ post_slack_sample/.env
	poetry run dev

test:
	poetry run pytest tests/

format:
	poetry run black post_slack_sample/ tests/

type-check:
	poetry run mypy -p post_slack_sample

export:
	poetry export -f requirements.txt --output requirements.txt

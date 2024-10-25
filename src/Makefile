###
# Run
###

run:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload

###
# Migrations
###

migrations:
	alembic revision --autogenerate

upgrade:
	alembic upgrade head



###
# Linter Tests
###

radon:
	poetry run radon mi -s -n B .

bandit:
	poetry run bandit -c pyproject.toml -r app

ruff:
	poetry run ruff check . --fix

mypy:
	poetry run mypy .

black:
	poetry run black .

ltest: black ruff mypy bandit radon


###
# Unit tests
###

pytest:
	DATABASE_URL="sqlite+aiosqlite:///:memory:" poetry run pytest



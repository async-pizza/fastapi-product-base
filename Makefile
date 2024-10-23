CUR_DIR=$(shell pwd)
VERSION_ENV=$(shell grep ^VERSION= .env | cut -d "=" -f 2-)
VERSION = $(shell echo $${VERSION:-$(VERSION_ENV)})
COMPOSE_PROJECT_NAME_ENV=$(shell grep ^COMPOSE_PROJECT_NAME= .env | cut -d "=" -f 2-)
COMPOSE_PROJECT_NAME = $(shell echo $${COMPOSE_PROJECT_NAME:-$(COMPOSE_PROJECT_NAME_ENV)})

##
# Backend
##

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

##
# Migrations
##

migrations:
	docker compose run --rm backend make migrations
upgrade:
	docker compose run --rm backend make upgrade


##
# Tests
##

mypy:
	docker compose run -it --rm backend make mypy

linter:
	docker compose run -it --rm backend make ltest

pytest:
	docker compose run -it --rm backend make pytest

ltest: mypy linter
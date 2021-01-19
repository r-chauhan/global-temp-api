SHELL=/bin/bash

.PHONY: bootstrap run run-docker lint test install

setup:
	python3 -m venv .venv && source .venv/bin/activate && \
	pip install -r requirements.txt

load-table:
	python3 ./src/load_mydb.py

run-docker:
	@docker-compose up

stop-docker:
	@docker-compose down

run-database:
	@docker-compose up db

test:
	@PYTHONPATH=. ENV=test pytest -v -s tests $(options)

lint:
	@flake8 resources/* tests/*

test:
	py.test -vv

db-revision:
	@FLASK_APP=src/main.py flask db revision --message $(message)

db-upgrade:
	@FLASK_APP=src/main.py flask db upgrade heads

db-upgrade-docker:
	@docker-compose run api make db-upgrade

db-client:
	@docker-compose exec postgres psql -U postgres $(database)

run-gunicorn:
	export POSTGRES_URL="127.0.0.1:5432" POSTGRES_DB="mydb" POSTGRES_USER="postgres" POSTGRES_PASSWORD="example" && \
	cd src && gunicorn main:app

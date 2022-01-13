build:
	 docker-compose build

test:
	docker-compose run --rm app python -m pytest -v

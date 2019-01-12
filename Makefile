run:
	# env $$(cat ops/env/development | xargs) flask run
	gunicorn wsgi -b 0.0.0.0:8000

db:
	docker run --rm -d -p 5432:5432 --name pg-test postgres
	# TODO: There should be a better way of doing this :/
	sleep 5
	docker exec -it pg-test createdb -U postgres -O postgres service
	alembic --config service/db/alembic.ini upgrade heads

test:
	pytest service/*/tests

clean:
	docker stop pg-test

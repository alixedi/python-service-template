run:
	env $$(cat ops/env/development | xargs) flask run

test:
	pytest service/*/tests

release:
	echo "Releasing new version and deploying to staging given CI clears"
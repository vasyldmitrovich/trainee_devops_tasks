TMP_FILE="temp_report.txt"
LOG_FILE="log.txt"
LOGFILE=app_log.txt

build:
	poetry install

test:
	poetry run coverage run -m unittest discover tests
	poetry run coverage report --fail-under=80 > $(TMP_FILE)

log:
	echo "---\nApp built successfully!" >> $(LOG_FILE)
	echo "Date: $$(date)" >> $(LOG_FILE)
	cat $(TMP_FILE) >> $(LOG_FILE)
	echo "---" >> $(LOG_FILE)
	rm $(TMP_FILE)

run:
	poetry run python my_app/app.py --logfile $(LOGFILE)
	echo "Sleeping for 2 seconds..."
	sleep 2

all: build run test log

# For testing
run-test-log: run test log

test-run-log: test run log
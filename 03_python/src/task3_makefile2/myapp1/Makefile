TMP_FILE="temp_report.txt"
LOG_FILE="log.txt"
LOGFILE=app_log.txt
DIRS=dir1 dir2 dir3

# This target installs all necessary dependencies using Poetry
build:
	poetry install

# This target runs tests and checks for 80% code coverage
test:
	poetry run coverage run -m unittest discover tests
	poetry run coverage report --fail-under=80 > $(TMP_FILE)

# This target logs the successful build and coverage report
log:
	echo "---\nApp built successfully!" >> $(LOG_FILE)
	@echo "Do not show in console"
	echo "Date: $$(date)" >> $(LOG_FILE)
	cat $(TMP_FILE) >> $(LOG_FILE)
	echo "---" >> $(LOG_FILE)
	rm $(TMP_FILE)

# This target runs the application and sleeps for 1 second
run:
	poetry run python my_app/app.py --logfile $(LOGFILE)
	echo "Sleeping for 2 seconds..."
	sleep 2

all: build run test log

# For testing, this target runs all necessary steps in sequence: run, test, log
run-test-log: run test log

test-run-log: test run log

# This target creates directories: dir1, dir2, dir3
create_dirs:
	mkdir -p $(DIRS)

# This target removes the created directories
clean_dirs:
	rm -rf $(DIRS)

# This target cleans up files; the 'edit' and '$(objects)' are placeholders
.PHONY: clean
clean: clean_dirs
#	-rm edit $(objects)  # 'edit' and '$(objects)' are placeholders, replace them with real file names

# Run python script with exception, use - of without -
exception:
	-python script.py
#	python script.py
	echo "---Finish running scenario, skip exception---"
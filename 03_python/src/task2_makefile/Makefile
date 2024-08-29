# This is a comment that specifies the Python interpreter
PYTHON=python3

# This variable contains the directory for Python source files
SRC_DIR=.

# This variable contains the directory for tests
TEST_DIR=tests

# This is the target to install dependencies
install:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

# This target runs the main Python script
run:
	@echo "Running the main Python script..."
	$(PYTHON) $(SRC_DIR)/main.py

# This target runs tests
test:
	@echo "Running tests..."
	$(PYTHON) -m unittest discover $(TEST_DIR)

# This target cleans up the project by removing __pycache__ and .pyc files
clean:
	@echo "Cleaning up..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Default target is to install dependencies, run the script, and then run tests
all: install run test

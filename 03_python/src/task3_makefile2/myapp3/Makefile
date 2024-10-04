# Define the Python interpreter
PYTHON = python3

# Define the path to the directory where this Makefile is located
MAKEFILE_DIR = $(abspath $(dir $(lastword $(MAKEFILE_LIST))))

# Use wildcard to find all Python files in the specified directory
SCRIPTS = $(wildcard $(MAKEFILE_DIR)/*.py)  # All .py files in the specified directory

# Target to run all Python scripts
run:
	@echo "Running all Python scripts from $(MAKEFILE_DIR)"
	@echo "Scripts: $(SCRIPTS)"
	@cd $(MAKEFILE_DIR) && \
	for script in *.py; do \
		$(PYTHON) $$script; \
	done

# Pattern rule for processing Python scripts
# This rule will be triggered for any .py file in the MAKEFILE_DIR
$(MAKEFILE_DIR)/%.py:
	@echo "Processing $< ..."
	@$(PYTHON) $<  # Execute the Python script


# Clean target to remove any temporary files if needed
clean:
	@echo "Cleaning up..."
	@rm -f $(SCRIPT_DIR)/*.pyc  # Remove compiled Python files
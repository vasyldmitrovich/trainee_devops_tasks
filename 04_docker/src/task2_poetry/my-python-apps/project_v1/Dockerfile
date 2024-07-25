# Use the official Python image
FROM python:3.9
LABEL authors="vbazh"

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy project files to the working directory
COPY AppLogV1.py pyproject.toml ./

# Install dependencies using Poetry
RUN poetry install

# Set environment variable for log directory path
ENV LOGS_DIR="/log_python_app_v1"

# Define a volume to persist logs
VOLUME ["${LOGS_DIR}"]

# Run the script, passing the log directory path
CMD ["poetry", "run", "python", "AppLogV1.py", "/log_python_app_v1/logs_v1.txt"]

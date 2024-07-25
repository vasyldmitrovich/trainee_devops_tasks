# Use the official Python image
FROM python:3.10
LABEL authors="vbazh"

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy project files to the working directory
COPY . /app

# Install dependencies using Poetry
RUN poetry install

# Set environment variable for log directory path
ENV LOGS_DIR="/log_python_app_v2"

# Define a volume to persist logs
VOLUME ["${LOGS_DIR}"]

# Run the script, passing the log directory path
CMD ["poetry", "run", "python", "AppLogV2.py", "/log_python_app_v2/logs_v2.txt"]

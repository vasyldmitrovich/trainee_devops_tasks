# Use the official Python image
FROM python:3.10

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy project files to the working directory
COPY . /app

# Install dependencies using Poetry
RUN poetry install

# Set environment variable for log directory path
ENV LOGS_DIR="/log_python_app"

# Run the script, passing the log directory path
CMD ["poetry", "run", "python", "AppLog.py", "/log_python_app/logs.txt"]

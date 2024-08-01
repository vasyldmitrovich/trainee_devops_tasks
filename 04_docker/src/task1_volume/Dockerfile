# Use the official Python image with support
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy files from the current directory to the working directory in the container
COPY AppLog.py .

# Set environment variable for the log directory path
ENV LOGS_DIR="/log_python_app"

# Execute the command to run the script, passing the path to the log directory
CMD ["python", "AppLog.py", "/log_python_app/logs.txt"]

# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Set environment variable for log directory path
ENV LOGS_DIR="/log_python_app"

# This container will just tail the log file
CMD ["tail", "-f", "/log_python_app/logs.txt"]

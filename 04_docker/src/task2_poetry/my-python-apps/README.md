# My Python App

This repository contains two separate Python applications, each using different versions of the `numpy` library. The projects demonstrate the use of logging, dependency management with Poetry, and application deployment using Docker containers.


- **project_v1**: The project that uses `numpy` version 1.19.5.
- **project_v2**: The project that uses `numpy` version 1.21.0.

## Installation and Running

Each project uses Poetry for dependency management and Docker for containerizing the applications.

### Installing Dependencies with Poetry

1. Navigate to the project directory (`project_v1` or `project_v2`).
2. Install Poetry if it is not already installed:
```bash
   pip install poetry
```

3. Install the dependency
```bash
   poetry install
```

### Running Projects Locally

Navigate to the project directory (project_v1 or project_v2).
Run the application:

```bash
poetry run python AppLogV1.py logs_v1.txt
```

or
```bash
poetry run python AppLogV2.py logs_v2.txt
```

Building and Running Docker Containers

Navigate to the project directory (___project_v1___ or ___project_v2___).

Build the Docker image:

```bash
docker build -t my-python-app-v1 .   # for project_v1
docker build -t my-python-app-v2 .   # for project_v2
```

Run the container with a volume for log storage:

For project_v1:

```bash
docker run --name app_v1 -v $(pwd)/logs_v1:/log_python_app_v1 my-python-app-v1
```

For project_v2:

```bash
docker run --name app_v2 -v $(pwd)/logs_v2:/log_python_app_v2 my-python-app-v2 
```

-v $(pwd)/logs_v1:/log_python_app_v1 and -v $(pwd)/logs_v2:/log_python_app_v2: 

Mount the local directory to the container directory, allowing logs to be stored on your local machine.

Logs

Logs are stored in the respective logs_v1 and logs_v2 directories for each project. 
The logs include information about the requests version used, the results of calculations, and any errors that occur.

Log Contents

Each run of the application generates a log file containing the following information:

    The numpy version used in the project.
    Informational messages about the calculation of the square of numbers.
    Error messages if incorrect data is provided.

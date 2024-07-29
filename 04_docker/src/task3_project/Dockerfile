FROM python:3.12-slim
LABEL authors="vbazh"

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="$HOME/.local/bin:$PATH"

WORKDIR /app

COPY ./* .

RUN poetry install --with test

CMD ["poetry", "run", "pytest"]
FROM python:3.12
LABEL authors="vbazh"

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="$HOME/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

ENV PATH="$PATH:/root/.local/bin"

RUN poetry install --with test

COPY . .

CMD ["poetry", "run", "pytest"]
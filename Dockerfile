# Build Stage
FROM python:3.12-slim AS builder

WORKDIR /build

COPY pyproject.toml .
COPY README.md .
COPY src ./src

RUN pip install --upgrade pip build
RUN python -m build

# Runtime Stage
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "orders_api.api:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "8000"]
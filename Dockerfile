FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock* ./

RUN uv sync --frozen

COPY . .

EXPOSE 8080

CMD ["sh", "-c", "exec uv run uvicorn src.api.rest.app:app --host 0.0.0.0 --port ${PORT:-8080}"]
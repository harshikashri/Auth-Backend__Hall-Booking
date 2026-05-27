FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency files first for better Docker cache usage
COPY pyproject.toml uv.lock* ./

# Install dependencies from pyproject.toml
RUN uv sync --frozen

# Copy project files
COPY . .

EXPOSE 8080

CMD ["sh", "-c", "exec uv run uvicorn src.api.rest.app:app --host 0.0.0.0 --port ${PORT:-8080}"]
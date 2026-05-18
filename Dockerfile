FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml ./

RUN python -m pip install --upgrade pip \
	&& python -m pip install \
		alembic>=1.18.4 \
		asyncpg>=0.31.0 \
		fastapi>=0.136.1 \
		python-jose[cryptography]>=3.3.0 \
		psycopg2-binary>=2.9.12 \
		pydantic-settings>=2.14.1 \
		python-dotenv>=1.2.2 \
		sqlalchemy[asyncio]>=2.0.49 \
		uvicorn>=0.47.0

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.rest.app:app", "--host", "0.0.0.0", "--port", "8000"]

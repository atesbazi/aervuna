# Pipeline worker image (used by infra/docker-compose.yml -> metar-archiver).
FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.11.32 /uv /uvx /bin/
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy PYTHONUNBUFFERED=1
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --no-install-project
COPY src ./src
RUN uv sync --frozen --no-dev
RUN useradd --system --uid 10001 pipeline
USER pipeline
ENTRYPOINT ["/app/.venv/bin/aervuna-pipeline"]

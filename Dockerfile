# ---------- Stage 1: build the virtual environment ----------
FROM python:3.12-slim AS builder

# uv for fast, reproducible installs. Pinned to the version that produced uv.lock.
COPY --from=ghcr.io/astral-sh/uv:0.13.9 /uv /bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Dependencies first, so this layer is cached when only code changes
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src ./src
COPY README.md ./
RUN uv sync --frozen --no-dev

# ---------- Stage 2: slim runtime image ----------
FROM python:3.12-slim AS runtime

# Run as a non-root user
RUN useradd --create-home --uid 1000 appuser
WORKDIR /app

COPY --from=builder --chown=appuser:appuser /app /app

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER appuser

# Replace with the project's real entry point (e.g. uvicorn for an API)
CMD ["python", "-m", "project_name.main"]

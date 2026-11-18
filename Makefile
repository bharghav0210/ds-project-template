# One-command workflow. Run `make help` to see everything.
# Windows: run these from Git Bash or WSL, or copy the command after each target.

PACKAGE := project_name
IMAGE   := project-name

.DEFAULT_GOAL := help
.PHONY: help setup lint format typecheck test test-fast run data docker-build docker-run clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-14s %s\n", $$1, $$2}'

setup: ## Install dependencies and git hooks
	uv sync
	uv run pre-commit install
	@test -f .env || cp .env.example .env
	@echo "Setup done. Edit .env if this project needs secrets."

lint: ## Lint and check formatting (what CI runs)
	uv run ruff check .
	uv run ruff format --check .

format: ## Auto-fix lint issues and format code
	uv run ruff check --fix .
	uv run ruff format .

typecheck: ## Static type checks
	uv run mypy src

test: ## Run all tests with coverage (fails under 70%)
	uv run pytest

test-fast: ## Run tests, skipping slow ones, no coverage
	uv run pytest -m "not slow" --no-cov

data: ## Download raw data (see scripts/download_data.py)
	uv run python scripts/download_data.py

run: ## Run the main entry point
	uv run python -m $(PACKAGE).main

docker-build: ## Build the Docker image
	docker build -t $(IMAGE) .

docker-run: ## Run the Docker image
	docker run --rm --env-file .env $(IMAGE)

clean: ## Remove caches and build artifacts
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov dist build
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +

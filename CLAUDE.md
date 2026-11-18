# CLAUDE.md

## Who I am and what this repo is for

I'm Bharghav, a data science student building a portfolio of production-grade projects in fintech risk, analytics and applied AI. This repo will be reviewed by recruiters and hiring managers. I must be able to explain every file and every decision in an interview, so working with me means teaching as you build, not just generating code.

The project's scope and acceptance criteria are in docs/SPEC.md. Read it before starting work.

## How to work with me

- Small steps. One logical change at a time (one feature, one test file, one model layer).
- After every step, run make lint and make test. Fix failures before moving on.
- Before every commit, stop and show me: the files changed, a 2–4 sentence plain-English explanation of what the change does and why, and a proposed commit message. Commit only after I say yes.
- Commit messages use conventional commits: feat:, fix:, test:, docs:, refactor:, chore:, build:, ci:. One logical change per commit.
- Explain decisions. When there's a real choice (split strategy, metric, library, schema), tell me the options and the trade-off in a few lines, then record it as an ADR in docs/adr/.
- Never invent results. Every number in the README, model card or docs must come from code that was actually run on the real data in this repo. If something hasn't been run, leave a TODO, not a guess.
- **No AI attribution in commits.** Never add Co-Authored-By or any other AI trailer to commit messages.

## Non-negotiable engineering standards

- **Structure:** real code in src/<package>/, tests in tests/, exploration only in numbered notebooks/ (01_eda.ipynb). Any logic worth keeping moves into src/ with a test.
- **Quality:** type hints on all public functions; logging, never print; configuration via config.py (pydantic-settings), never hard-coded paths, seeds or keys.
- **Testing:** pytest unit tests for every transform, feature and business rule; at least one integration test of the whole pipeline on a small fixture; data validation (pandera or dbt tests); coverage ≥ 70% on src/.
- **Data:** raw data lives outside the repo or in git-ignored data/raw/. Never commit data, model binaries, .env, venv/, \_\_pycache\_\_/ or logs. scripts/download_data.py documents the source and licence.
- **ML work:** time-based (or group-based) splits where time matters; a rule-based or simple baseline before any complex model; fit preprocessing on training data only; check every feature for target leakage; report metrics with confidence intervals; log runs to MLflow when the spec asks for it.
- **LLM work:** build the evaluation set before tuning; measure every change against it; validate outputs with pydantic; track cost and latency.
- **APIs:** FastAPI with pydantic request/response schemas, /health, proper error codes.
- **Reproducibility:** fixed random seeds from config; a fresh clone must work with make setup && make test && make run.

## Docs to keep current as we go

- README.md: problem, headline result vs baseline, data, approach, results table, limitations, how to run.
- docs/design.md: architecture and trade-offs.
- docs/adr/: one short ADR per real decision.
- docs/model_card.md: for any project with a model.

## Things to avoid

- Big-bang changes that touch many files at once.
- Buzzword names or claims ("enterprise", "AI-powered", "state-of-the-art").
- Accuracy as the headline metric on imbalanced data.
- Random train/test splits on time-ordered data.
- Adding dependencies without telling me why.

# project-name: One line: the problem this project solves.

![CI](https://github.com/bharghav0210/project-name/actions/workflows/ci.yml/badge.svg)
[Live demo](#) · [Design doc](docs/design.md) · [Model card](docs/model_card.md)

**Problem.** One paragraph: who has the problem, what it costs them, and what decision this project makes or supports.

**Result.** One line with the headline number against the baseline.
> TODO: <metric> for the final model vs <baseline>, from run <id>

<!-- ![demo](docs/demo.gif) -->

## Architecture

Diagram (docs/architecture.png) plus 3–4 sentences on how the parts fit together.

## Data

| | |
| --- | --- |
| Source | [name](link) |
| Licence | |
| Size | rows, columns, time range |
| Known issues | |

Download with `make data`. Raw data is never committed.

## Approach

The lifecycle stages in order, one short paragraph each: framing, data checks, split, baselines, features, models, evaluation.

## Results

| Model | Primary metric (95% CI) | Secondary metric | Latency |
| --- | --- | --- | --- |
| Baseline | | | |
| Final model | | | |

Every number here is reproducible from a run ID or commit hash.

## Limitations

What this does not handle, and where it would fail.

## Run it

```bash
make setup      # install dependencies and git hooks
make data       # download raw data
make test       # tests + coverage
make run        # run the pipeline
```

No `make` (Windows)? Run the command shown under each target in the `Makefile`.

## Project structure

```
src/project_name/   package code (the source of truth)
tests/              unit and integration tests
notebooks/          numbered exploration notebooks only
scripts/            data download and one-off utilities
configs/            configuration files
docs/               design doc, ADRs, model card
```

## With more time

- Next improvement, and why it matters

## Licence

MIT

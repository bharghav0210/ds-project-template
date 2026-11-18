"""Entry point. Replace run() with the project's real pipeline steps."""

import logging

from project_name.config import get_settings
from project_name.logging_config import setup_logging

logger = logging.getLogger(__name__)


def run() -> dict[str, str]:
    """Run the pipeline and return a small summary (handy for tests)."""
    settings = get_settings()
    logger.info("Starting in %s mode, data dir: %s", settings.app_env, settings.data_dir)
    # TODO: call the real steps, e.g. load -> validate -> transform -> train -> evaluate
    return {"status": "ok", "env": settings.app_env}


def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)
    summary = run()
    logger.info("Finished: %s", summary)


if __name__ == "__main__":
    main()

"""Logging setup. Use `logger = logging.getLogger(__name__)` in every module, never print()."""

import logging
import sys

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def setup_logging(level: str = "INFO") -> None:
    """Configure the root logger once, at the program's entry point."""
    logging.basicConfig(
        level=level.upper(),
        format=LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
        force=True,
    )

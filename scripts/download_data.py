"""Download the raw data for this project into data/raw/.

Fill in DATASET for each project. Raw data is never committed: this script is how anyone,
including CI or a reviewer, gets the exact same files.

Kaggle datasets need the Kaggle CLI and an API token:
    uv add --dev kaggle
    # put kaggle.json in ~/.kaggle/ (Windows: C:\\Users\\<you>\\.kaggle\\) - it is git-ignored
"""

import logging
import subprocess
import sys

from project_name.config import get_settings
from project_name.logging_config import setup_logging

logger = logging.getLogger(__name__)

# Fill these in per project, and copy the licence and size into the README's Data section.
DATASET = {
    "kaggle_slug": "",  # e.g. "olistbr/brazilian-ecommerce"
    "source_url": "",  # the dataset's public page
    "licence": "",
}


def download_from_kaggle(slug: str) -> None:
    raw_dir = get_settings().raw_dir
    raw_dir.mkdir(parents=True, exist_ok=True)
    logger.info("Downloading %s into %s", slug, raw_dir)
    subprocess.run(
        ["kaggle", "datasets", "download", "-d", slug, "-p", str(raw_dir), "--unzip"],
        check=True,
    )


def main() -> None:
    setup_logging(get_settings().log_level)
    if not DATASET["kaggle_slug"]:
        logger.error("Set DATASET['kaggle_slug'] in scripts/download_data.py first.")
        sys.exit(1)
    download_from_kaggle(DATASET["kaggle_slug"])
    logger.info("Done. Files are in %s", get_settings().raw_dir)


if __name__ == "__main__":
    main()

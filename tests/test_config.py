import pytest
from pydantic import ValidationError

from project_name.config import Settings, get_settings


def test_env_vars_override_defaults() -> None:
    settings = get_settings()
    assert settings.app_env == "test"


def test_derived_paths_sit_under_data_dir() -> None:
    settings = get_settings()
    assert settings.raw_dir == settings.data_dir / "raw"
    assert settings.processed_dir.parent == settings.data_dir


def test_invalid_values_are_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(random_seed=-1)
    with pytest.raises(ValidationError):
        Settings(app_env="staging")  # type: ignore[arg-type]


def test_settings_are_cached() -> None:
    assert get_settings() is get_settings()

import pytest

from project_name.main import main, run


def test_run_returns_summary() -> None:
    assert run() == {"status": "ok", "env": "test"}


@pytest.mark.integration
def test_main_runs_end_to_end(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    out = capsys.readouterr().out
    assert "Starting in test mode" in out
    assert "Finished" in out

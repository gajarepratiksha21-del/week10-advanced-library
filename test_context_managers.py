
from my_advanced_lib.core.context_managers import (
    open_file,
    read_text,
    temporary_setting,
)


def test_open_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello Python", encoding="utf-8")

    with open_file(str(file_path)) as file:
        assert file.read() == "Hello Python"


def test_read_text(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Welcome", encoding="utf-8")

    assert read_text(str(file_path)) == "Welcome"


def test_temporary_setting_existing_key():
    settings = {"theme": "light"}

    with temporary_setting(settings, "theme", "dark"):
        assert settings["theme"] == "dark"

    assert settings["theme"] == "light"


def test_temporary_setting_new_key():
    settings = {}

    with temporary_setting(settings, "language", "English"):
        assert settings["language"] == "English"

    assert "language" not in settings


def test_temporary_setting_after_exception():
    settings = {"mode": "normal"}

    try:
        with temporary_setting(settings, "mode", "advanced"):
            raise ValueError("Test error")
    except ValueError:
        pass

    assert settings["mode"] == "normal"


from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def open_file(filepath: str, mode: str = "r") -> Iterator:
    """Open a file and close it automatically."""
    with open(filepath, mode, encoding="utf-8") as file:
        yield file


@contextmanager
def temporary_setting(
    settings: dict, key: str, value: object
) -> Iterator[dict]:
    """Temporarily change a dictionary setting."""
    existed = key in settings
    old_value = settings.get(key)

    settings[key] = value

    try:
        yield settings
    finally:
        if existed:
            settings[key] = old_value
        else:
            settings.pop(key, None)


def read_text(filepath: str) -> str:
    """Read text from a file."""
    with open_file(filepath) as file:
        return file.read()

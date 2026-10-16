
import pytest

from my_advanced_lib.core.decorators import (
    cache,
    retry,
    timer,
    validate_positive,
)
from my_advanced_lib.exceptions import RetryError


def test_timer():
    @timer
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_retry_success():
    @retry(max_attempts=3)
    def greet():
        return "Hello"

    assert greet() == "Hello"


def test_retry_failure():
    @retry(max_attempts=2)
    def fail():
        raise ValueError("Failed")

    with pytest.raises(RetryError):
        fail()


def test_retry_invalid_attempts():
    with pytest.raises(ValueError):
        retry(max_attempts=0)


def test_cache():
    calls = []

    @cache
    def add(a, b):
        calls.append(1)
        return a + b

    assert add(2, 3) == 5
    assert add(2, 3) == 5
    assert len(calls) == 1


def test_validate_positive():
    @validate_positive
    def square(n):
        return n * n

    assert square(4) == 16


def test_validate_positive_negative():
    @validate_positive
    def square(n):
        return n * n

    with pytest.raises(ValueError):
        square(-4)

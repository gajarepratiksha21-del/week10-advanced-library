
import pytest

from my_advanced_lib.core.generators import (
    batch_generator,
    fibonacci_generator,
    filter_positive,
)


def test_batch_generator():
    result = list(batch_generator([1, 2, 3, 4, 5], 2))
    assert result == [[1, 2], [3, 4], [5]]


def test_batch_generator_empty():
    assert list(batch_generator([], 2)) == []


def test_batch_generator_invalid_size():
    with pytest.raises(ValueError):
        list(batch_generator([1, 2], 0))


def test_fibonacci_generator():
    result = list(fibonacci_generator(7))
    assert result == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_generator_zero():
    assert list(fibonacci_generator(0)) == []


def test_fibonacci_generator_negative():
    with pytest.raises(ValueError):
        list(fibonacci_generator(-1))


def test_filter_positive():
    result = list(filter_positive([-2, 0, 1, 3, -5]))
    assert result == [1, 3]


def test_filter_positive_empty():
    assert list(filter_positive([])) == []

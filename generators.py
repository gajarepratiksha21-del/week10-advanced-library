
from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def batch_generator(
    items: Iterable[T], batch_size: int = 100
) -> Iterator[list[T]]:
    """Yield items in batches."""
    if batch_size < 1:
        raise ValueError("batch_size must be positive")

    batch: list[T] = []

    for item in items:
        batch.append(item)

        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch


def fibonacci_generator(limit: int) -> Iterator[int]:
    """Generate a Fibonacci sequence."""
    if limit < 0:
        raise ValueError("limit cannot be negative")

    a, b = 0, 1

    for _ in range(limit):
        yield a
        a, b = b, a + b


def filter_positive(items: Iterable[int]) -> Iterator[int]:
    """Yield only positive numbers."""
    for item in items:
        if item > 0:
            yield item

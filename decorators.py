
import functools
import logging
import time
from collections.abc import Callable
from typing import Any, ParamSpec, TypeVar

from my_advanced_lib.exceptions import RetryError

P = ParamSpec("P")
T = TypeVar("T")

logger = logging.getLogger(__name__)


def timer(func: Callable[P, T]) -> Callable[P, T]:
    """Measure and log function execution time."""

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info("%s took %.4f seconds", func.__name__, elapsed)
        return result

    return wrapper


def retry(max_attempts: int = 3) -> Callable:
    """Retry a function when it raises an exception."""

    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    def decorator(func: Callable[P, T]) -> Callable[P, T]:

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    if attempt == max_attempts - 1:
                        raise RetryError(
                            f"{func.__name__} failed after {max_attempts} attempts"
                        ) from error

            raise RetryError("Unexpected retry error")

        return wrapper

    return decorator


def cache(func: Callable[P, T]) -> Callable[P, T]:
    """Cache results for repeated calls with the same arguments."""
    results: dict[Any, T] = {}

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        key = (args, tuple(sorted(kwargs.items())))

        try:
            if key not in results:
                results[key] = func(*args, **kwargs)
            return results[key]
        except TypeError:
            return func(*args, **kwargs)

    return wrapper


def validate_positive(func: Callable[P, T]) -> Callable[P, T]:
    """Reject negative numeric arguments."""

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        for value in (*args, *kwargs.values()):
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                if value < 0:
                    raise ValueError("Arguments cannot be negative")
        return func(*args, **kwargs)

    return wrapper

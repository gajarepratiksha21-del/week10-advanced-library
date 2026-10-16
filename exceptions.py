
class RetryError(Exception):
    """Raised when a function fails after all retry attempts."""


class ValidationError(Exception):
    """Raised when data validation fails."""


class SerializationError(Exception):
    """Raised when data serialization fails."""

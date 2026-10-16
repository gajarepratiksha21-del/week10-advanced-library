
import json
from typing import Any

from my_advanced_lib.exceptions import SerializationError


def serialize(data: dict[str, Any]) -> str:
    try:
        return json.dumps(data)
    except (TypeError, ValueError) as error:
        raise SerializationError("Unable to serialize data") from error


def deserialize(data: str) -> dict[str, Any]:
    try:
        result = json.loads(data)

        if not isinstance(result, dict):
            raise SerializationError("Data must be a JSON object")

        return result

    except json.JSONDecodeError as error:
        raise SerializationError("Invalid JSON data") from error

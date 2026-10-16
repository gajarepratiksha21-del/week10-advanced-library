
from my_advanced_lib.exceptions import ValidationError


def validate_name(name: str) -> bool:
    if not isinstance(name, str) or not name.strip():
        raise ValidationError("Name cannot be empty")
    return True


def validate_age(age: int) -> bool:
    if not isinstance(age, int) or isinstance(age, bool) or age < 0:
        raise ValidationError("Age must be a non-negative integer")
    return True


def validate_email(email: str) -> bool:
    if not isinstance(email, str) or "@" not in email or "." not in email:
        raise ValidationError("Invalid email address")
    return True

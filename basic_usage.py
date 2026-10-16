
import logging

from my_advanced_lib import (
    timer,
    retry,
    batch_generator,
    fibonacci_generator,
    temporary_setting,
    serialize,
    deserialize,
    validate_name,
    validate_age,
    validate_email,
    GreetingPlugin,
)

logging.basicConfig(level=logging.INFO)


@timer
def add(a, b):
    return a + b


@retry(max_attempts=3)
def greet():
    return "Hello, Python!"


def main():
    print("Decorator Example:")
    print(add(10, 20))
    print(greet())

    print("\nGenerator Example:")
    print(list(fibonacci_generator(7)))
    print(list(batch_generator([1, 2, 3, 4, 5], 2)))

    print("\nValidation Example:")
    print(validate_name("Pratiksha"))
    print(validate_age(21))
    print(validate_email("test@example.com"))

    print("\nSerialization Example:")
    data = {"name": "Pratiksha", "course": "Python"}
    json_data = serialize(data)
    print(json_data)
    print(deserialize(json_data))

    print("\nContext Manager Example:")
    settings = {"theme": "light"}

    with temporary_setting(settings, "theme", "dark"):
        print("Temporary setting:", settings["theme"])

    print("Restored setting:", settings["theme"])

    print("\nPlugin Example:")
    plugin = GreetingPlugin()
    print(plugin.run())


if __name__ == "__main__":
    main()

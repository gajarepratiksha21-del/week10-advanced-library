
from my_advanced_lib import (
    batch_generator,
    fibonacci_generator,
    serialize,
    deserialize,
    validate_name,
    validate_age,
    validate_email,
    GreetingPlugin,
    get_plugins,
)


def test_serialization_integration():
    data = {"name": "Pratiksha", "age": 21}

    result = serialize(data)
    restored = deserialize(result)

    assert restored == data


def test_validation_integration():
    assert validate_name("Pratiksha") is True
    assert validate_age(21) is True
    assert validate_email("test@example.com") is True


def test_generators_integration():
    assert list(fibonacci_generator(5)) == [0, 1, 1, 2, 3]
    assert list(batch_generator([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_plugin_integration():
    plugin = GreetingPlugin()

    assert plugin.run() == "Hello from the plugin!"
    assert "GreetingPlugin" in get_plugins()

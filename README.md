
# Advanced Python Library

A Python library demonstrating advanced Python concepts, including decorators, generators, context managers, metaclasses, data validation, serialization, and automated testing.

## Project Description

The Advanced Python Library is designed to demonstrate reusable Python components and advanced programming techniques. It includes utility functions, custom exceptions, plugin registration, and automated tests to ensure code quality and reliability.

## Features

- **Decorators:** Timer, retry, caching, and positive-value validation.
- **Generators:** Fibonacci sequence, batch processing, and positive-value filtering.
- **Context Managers:** File handling and temporary settings management.
- **Metaclasses:** Plugin registration and management.
- **Data Validation:** Name, age, and email validation.
- **Serialization:** Convert Python objects to JSON and deserialize JSON data.
- **Custom Exceptions:** Handle retry, validation, and serialization errors.
- **Automated Testing:** Test library functionality using pytest.
- **Code Coverage:** Measure test coverage using pytest-cov.
- **Benchmarking:** Measure the performance of selected functions.

## Technologies Used

- Python 3.10+
- pytest
- pytest-cov
- setuptools
- JSON
- Git and GitHub
- GitHub Actions

## Project Structure

```text
week10-advanced-library/
├── src/
│   └── my_advanced_lib/
│       ├── __init__.py
│       ├── exceptions.py
│       ├── types.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── decorators.py
│       │   ├── generators.py
│       │   ├── context_managers.py
│       │   └── metaclasses.py
│       └── utils/
│           ├── __init__.py
│           ├── validators.py
│           └── serializers.py
├── tests/
│   ├── test_decorators.py
│   ├── test_generators.py
│   ├── test_context_managers.py
│   └── test_integration.py
├── examples/
│   └── basic_usage.py
├── scripts/
│   └── benchmark.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── pyproject.toml
├── setup.py
├── requirements-dev.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Open the Project Directory

```bash
cd week10-advanced-library
```

### 3. Install the Library

```bash
py -m pip install -e .
```

### 4. Install Development Dependencies

```bash
py -m pip install -r requirements-dev.txt
```

## Usage Examples

### 1. Using Decorators

```python
from my_advanced_lib import timer, retry

@timer
def add(a, b):
    return a + b

print(add(10, 20))
```

### 2. Using Generators

```python
from my_advanced_lib import fibonacci_generator

print(list(fibonacci_generator(7)))
```

### 3. Using Data Validation

```python
from my_advanced_lib import validate_name, validate_age, validate_email

print(validate_name("Pratiksha"))
print(validate_age(21))
print(validate_email("student@example.com"))
```

### 4. Using Serialization

```python
from my_advanced_lib import serialize, deserialize

data = {"name": "Pratiksha", "course": "Python"}

json_data = serialize(data)
print(json_data)

original_data = deserialize(json_data)
print(original_data)
```

### 5. Using Context Managers

```python
from my_advanced_lib import temporary_setting

settings = {"theme": "light"}

with temporary_setting(settings, "theme", "dark"):
    print(settings["theme"])

print(settings["theme"])
```

## Running the Examples

Run the example program from the project root:

```bash
py examples/basic_usage.py
```

## Running Tests

Run all tests:

```bash
py -m pytest -v
```

Run tests with code coverage:

```bash
py -m pytest --cov=my_advanced_lib --cov-report=term-missing
```

## Test Results

The project has successfully completed **24 automated tests** with **93% total code coverage** in the local test run.

Coverage and test results may vary when the code or testing environment changes.

## Benchmarking

Run the benchmark script:

```bash
py scripts/benchmark.py
```

This script measures the execution time of selected generator operations.

## Continuous Integration

GitHub Actions is configured to run automated tests when code is pushed or a pull request is opened. The workflow tests the library using Python 3.10 and Python 3.13.

## Learning Outcomes

Through this project, I learned:

1. How to create reusable Python packages.
2. How to implement decorators and generators.
3. How to use context managers for resource management.
4. How to work with metaclasses and plugin registration.
5. How to validate and serialize data.
6. How to create custom exceptions.
7. How to write automated tests using pytest.
8. How to measure code coverage and benchmark performance.
9. How to automate testing with GitHub Actions.

## Author

**Pratiksha Gajare**

Python Development | Advanced Python Concepts | Software Testing

## License

This project is intended for educational and learning purposes.


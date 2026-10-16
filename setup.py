
from setuptools import setup, find_packages

setup(
    name="my-advanced-lib",
    version="0.1.0",
    description="An advanced Python library demonstrating advanced concepts",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
)

"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages


def long_description():
    with open("README.md") as fp:
        return fp.read()


version = __import__("DuckDuck.__init__").__version__
setup(
    name="DuckDuck",
    author="iamSkev",
    author_email="shawnkenzov@gmail.com",
    url="https://github.com/iamSkev/duck",
    description="An async API wrapper for the Random-d.uk API",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    version=version,
    packages=find_packages(where=".", exclude=["tests"]),
    keywords=["duck", "randomduck", "randomduk", "duckapi"],
    install_requires=[
        "aiofiles>=0.8.0",
        "aiohttp>=3.8.1",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
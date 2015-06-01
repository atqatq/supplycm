"""Setup script for supplycm."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="supplycm",
    version="0.1.0",
    description="Supply Chain Management algorithms (pure Python, no dependencies)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="supplycm",
    author_email="supplycm.dev@gmail.com",
    url="https://github.com/supplycm/supplycm",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.6",
)

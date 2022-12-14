import os
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='datadog-pandas',
    version='0.1.0',
    description='Pandas integration for Datadog',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LemontechSA/datadog-pandas',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

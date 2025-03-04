"""Package installer."""
import os
from setuptools import setup
from setuptools import find_packages

LONG_DESCRIPTION = ""
if os.path.exists("README.md"):
    with open("README.md") as fp:
        LONG_DESCRIPTION = fp.read()

scripts = []

setup(
    name="mobpredict",
    version="0.0.1",
    description="Next location prediction",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Ye Hong",
    author_email=("hongy@ethz.ch"),
    license="Apache-2.0",
    url="https://github.com/irmlma/next-location-prediction",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 1 - Planning",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages("."),
    python_requires=">=3.9",
)

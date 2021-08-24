#!/usr/bin/python3
# encoding: utf-8
"""A setuptools based setup module for password_bank"""

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open(path.join(here, "HISTORY.md"), encoding="utf-8") as history_file:
    history = history_file.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as requirements_file:
    requirements = requirements_file.read()

with open(path.join(here, "requirements_dev.txt"), encoding="utf-8") as requirements_dev_file:
    requirements_dev = requirements_dev_file.read()

ext_modules = []
setup(
    name="password_bank",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="store your password",
    long_description=readme + "\n\n" + history,
    author="AngusWG",
    author_email="z740713651@outlook.com",
    url="https://github.com/AngusWG/password-bank",
    packages=find_packages(include=["password_bank", "password_bank.*"]),
    entry_points={
        "console_scripts": [
            "password_bank=password_bank.__main__:entry_point",
            "pbank=password_bank.__main__:entry_point",
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require={"dev_require": requirements + "\n" + requirements_dev},
    ext_modules=ext_modules,
    keywords="password_bank",
)

#!/usr/bin/python3
# encoding: utf-8
from __future__ import print_function

from ._version import get_versions

__author__ = "AngusWG"
__email__ = "z740713651@outlook.com"
__version__ = get_versions()["version"]
del get_versions

from password_bank.core import PasswordBank

PasswordBank

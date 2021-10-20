#!/usr/bin/python3
# encoding: utf-8

"""
test_value_bank
----------------------------------

Tests for `value_bank` module.
"""
import os

import pytest

from value_bank.cli_helper import CliHelper


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get("https://github.com/audreyr/cookiecutter-pypackage")


class TestValue_bank:
    @classmethod
    def setup_class(cls):
        current = os.getcwd()
        _config_file: str = os.path.join(current, ".v_bank.json")
        _store_file: str = os.path.join(current, ".v_bank_store.json")
        cls.cli_helper = CliHelper(_config_file, _store_file)

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_bank(self):
        default = [
            ("192.168.0.122", "user_1", "passwd2"),
            ("192.168.0.68", "user_1", "passwd3"),
            ("192.168.0.13", "user_2", "passwd2"),
            ("mysql", "root", "passwd4"),
            ("sentry", "user_2", "123456"),
            ("wiki", "user_3", "passwd"),
            ("test_jenkins", "field_1", "passwd5"),
            ("jenkins", "zza", "passwd"),
            ("导航", "field_1", "passwd5"),
        ]
        # loading
        for args in default:
            self.cli_helper(*args, force=True)
        self.cli_helper("field_1", "passwd5")
        # asset
        res = self.cli_helper("sentry")
        assert "sentry" in res.keys
        assert res.main_key == "user_2"
        res = self.cli_helper("user_3")
        assert res.main_key == "user_3"
        # find
        res = self.cli_helper.find("user_1")
        assert len(res) == 2
        # delete
        self.cli_helper.rm("user_3", force=True)
        res = self.cli_helper("user_3")
        assert res is None
        # version
        self.cli_helper.version()

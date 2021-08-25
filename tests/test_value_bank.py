#!/usr/bin/python3
# encoding: utf-8

"""
test_value_bank
----------------------------------

Tests for `value_bank` module.
"""
import pytest


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
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_bank(self):
        from value_bank.__main__ import main

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
            main(*args, force=True)
        main("field_1", "passwd5")
        # asset
        res = main("sentry")
        assert "sentry" in res.keys
        assert res.account == "user_2"
        res = main("user_3")
        assert res.account == "user_3"
        # find
        res = main("find", "user_1")
        assert len(res) == 2
        # delete
        main("del", "user_3", force=True)
        res = main("user_3")
        assert res is None

        # version
        main("version")

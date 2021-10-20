#!/usr/bin/python3
# encoding: utf-8
""" value_bank 's entry_points"""

import fire


def entry_point() -> None:  # pragma: no cover
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    from value_bank.cli_helper import CliHelper
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    content = CliHelper()
    fire.Fire(content)
    del content


if __name__ == "__main__":
    entry_point()

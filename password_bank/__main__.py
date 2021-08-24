#!/usr/bin/python3
# encoding: utf-8
""" password_bank 's entry_points"""
import functools
from typing import Any, Callable

import fire

from password_bank import PasswordBank


def entry_point() -> None:  # pragma: no cover
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(main)


bank: PasswordBank = PasswordBank.read()


def save_wrapper(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        res = func(*args, **kwargs)
        bank.store()
        return res

    return wrapper


@save_wrapper
def main(*fields: str, force: bool = False) -> Any:
    key = fields[0]
    if key == "version":
        return version()

    elif key == "del":
        return bank.delete(fields[1], force=force)

    elif key == "find":
        return bank.find(fields[1])

    if len(fields) == 1:
        return bank.get(key)
    else:
        return bank.set_key(fields, force)


def version() -> str:
    """显示当前版本"""
    import password_bank

    return password_bank.__version__


if __name__ == "__main__":
    entry_point()

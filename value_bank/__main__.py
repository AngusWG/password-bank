#!/usr/bin/python3
# encoding: utf-8
""" value_bank 's entry_points"""
import functools
from typing import Any, Callable

import fire

from value_bank.core import Bank, Content


def entry_point() -> None:  # pragma: no cover
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(main)


content = Content()
bank: Bank = content.bank


def save_wrapper(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        res = func(*args, **kwargs)
        global content
        del content
        return res

    return wrapper


@save_wrapper
def main(*fields: str, force: bool = False) -> Any:
    """
    value_bank is use to store/get value by keys to your clipboard

    Examples:
        set: > vbank ubuntu root 123456
             V(main_key=root, value=123456, ex_keys=['ubuntu'])

        get: > vbank ubuntu
             V(main_key=root, value=123456, ex_keys=['ubuntu'])
             # your clipboard is root

        get: > vbank root
             V(main_key=root, value=123456, ex_keys=['ubuntu'])
             # your clipboard is 123456

        del: > vbank del ubuntu # or vbank del root
             > Are you sure to delete V(main_key=root, value=123456, ex_keys=['ubuntu'])? (y/n) y

        find:> vbank find ubuntu
             V(main_key=root, value=111111, ex_keys=['win'])
             V(main_key=root, value=123123, ex_keys=['centos'])

        gist: vbank gist token aaabbbcc
    """
    if len(fields) == 0:
        return main.__doc__
    key = fields[0]
    if key == "version":
        return version()

    elif key == "del":
        return bank.delete(fields[1], force=force)

    elif key == "find":
        return bank.find(fields[1])

    elif key == "clean":
        return bank.clean()

    elif key == "gist":
        return content.conf.set_token(fields[1])

    elif key == "pin":
        return content.use_password(fields[1])

    if len(fields) == 1:
        return bank.get(key)
    else:
        return bank.set_key(fields, force)


def version() -> str:
    """显示当前版本"""
    import value_bank

    return value_bank.__version__


if __name__ == "__main__":
    entry_point()

#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/10/20 15:59
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : encrypt_utils.py

import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


def _format_key(value: str) -> bytes:
    """需要补位，str不是16的倍数那就补足为16的倍数"""
    password = value.encode()
    hkdf = HKDF(
        algorithm=hashes.SHA256(),  # You can swap this out for hashes.MD5()
        length=32,
        salt=None,  # You may be able to remove this line but I'm unable to test
        info=None,  # You may also be able to remove this line
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(hkdf.derive(password))
    return key


def encrypt(key: str, text: str) -> str:
    """加密方法"""
    fer = Fernet(_format_key(key))
    token = fer.encrypt(text.encode()).decode()
    return token


def decrypt(key: str, text: str) -> str:
    """解密方法"""
    fer = Fernet(_format_key(key))
    return fer.decrypt(text.encode()).decode()


if __name__ == "__main__":
    tmp_key = "v_bank"
    content = "one python one day."
    en_text = encrypt(tmp_key, content)
    de_text = decrypt(tmp_key, en_text)
    print(en_text)
    print(de_text)

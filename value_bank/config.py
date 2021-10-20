#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/10/20 11:25
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : config.py
import base64
import os
from typing import Optional

from Crypto.Cipher import AES
from pydantic import BaseModel

from value_bank.gist_utils import download_gists, upload_gists

config_file = os.path.join(os.path.expanduser("~"), ".v_bank.json")


def add_to_16(value):
    """需要补位，str不是16的倍数那就补足为16的倍数"""
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


def encrypt(key, text):
    """加密方法"""
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    encrypt_aes = aes.encrypt(add_to_16(text))  # 先进行aes加密
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text


def decrypt(key, text):
    """解密方法"""
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))  # 优先逆向解密base64成bytes
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
    return decrypted_text


class Config(BaseModel):
    use_password: bool = False
    gist_token: Optional[str] = None

    def store(self) -> str:
        with open(config_file, "w+", encoding="utf-8") as f:
            f.write(self.json(indent=4))
        return config_file

    @classmethod
    def read(cls) -> "Config":
        if os.path.exists(config_file):
            return cls.parse_file(config_file)
        else:
            return cls()

    def set_token(self, token):
        self.gist_token = token

    def update(self, content: str, password: str = None):
        if not self.gist_token:
            return
        if self.use_password:
            content = encrypt(password, content)
        upload_gists(self.gist_token, content)

    def download(self, password: str = None):
        if not self.gist_token:
            return
        content = download_gists(self.gist_token)
        if self.use_password:
            content = decrypt(password, content)
        return content

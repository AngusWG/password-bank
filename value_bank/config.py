#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/10/20 11:25
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : config.py
import os
from typing import Optional

from pydantic import BaseModel

from value_bank.gist_utils import download_gists, upload_gists


class Config(BaseModel):
    use_password: bool = False
    gist_token: Optional[str] = None

    def store(self, config_file: str) -> str:
        with open(config_file, "w+", encoding="utf-8") as f:
            f.write(self.json(indent=4))
        return config_file

    @classmethod
    def read(cls, config_file: str) -> "Config":
        if os.path.exists(config_file):
            return cls.parse_file(config_file)
        else:
            return cls()

    def update_to_gist(self, content: str) -> Optional[str]:
        if not self.gist_token:
            return
        return upload_gists(self.gist_token, content)

    def download_to_file(self, store_file: str) -> None:
        if not self.gist_token:
            return
        content = download_gists(self.gist_token)
        with open(store_file, "w+", encoding="utf-8") as f:
            f.write(content)

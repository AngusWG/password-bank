import datetime
import os
from typing import Dict, List, Optional, Tuple, Union

from prompt_toolkit.clipboard import pyperclip
from pydantic import BaseModel


class Account(BaseModel):
    account: str
    password: str
    keys: List[str] = []
    account_id: datetime.datetime = datetime.datetime.now()

    def __repr__(self):
        return f"Account(account={self.account}, password={self.password}, keys={self.keys})"


store_file = os.path.join(os.path.dirname(__file__), "store.json")


class PasswordBank(BaseModel):
    accounts: List[Account] = list()
    keys: Dict[str, Account] = dict()
    last: Optional[Account] = None

    def store(self) -> str:
        with open(store_file, "w+", encoding="utf-8") as f:
            f.write(self.json(indent=4))
        return store_file

    @classmethod
    def read(cls) -> "PasswordBank":
        if os.path.exists(store_file):
            return cls.parse_file(store_file)
        else:
            return cls()

    def set_key(
        self, fields: Tuple[str, ...], force: bool = False
    ) -> Union[str, Account]:
        if len(fields) == 2:
            account, password = fields
            key = None
        elif len(fields) == 3:
            key, account, password = fields
        else:  # fields > 3 or fields < 2:
            return "Error: invalid number of fields"

        if key in self.keys:
            self._delete_account(self.keys[key], force=force)
        print("fields", fields)
        account = Account(account=account, password=password)
        self.accounts.append(account)

        if key:
            self.keys[key] = account
            account.keys.append(key)
            return account
        return account

    def get(self, key: str) -> Optional[Account]:
        if self.last and key == self.last.account:
            pyperclip.pyperclip.copy(self.last.password)
            return self.last
        if key in self.keys:
            account = self.keys[key]
            pyperclip.pyperclip.copy(account.account)
            self.last = account
            return account
        else:
            for account in self.accounts:
                if key == account.account:
                    pyperclip.pyperclip.copy(account.password)
                    self.last = account
                    return account
        return None

    def find(self, key: str) -> List[Account]:
        res = []
        for _key in self.keys:
            if key in _key:
                res.append(self.keys[_key])
        for account in self.accounts:
            if key in account.account or key in account.password:
                res.append(account)
        return res

    def delete(self, key: str, force: bool = False) -> str:
        if key in self.keys:
            self._delete_account(self.keys[key], force)
            return "delete"
        else:
            for account in self.accounts:
                if key == account.account or key in account.password:
                    self._delete_account(account, force)
            return "delete"

    def _delete_account(self, account: Account, force: bool = False) -> bool:
        if force or input("Are you sure to delete {}? (y/n) ".format(account)) == "y":
            self.accounts.remove(account)
            for key in account.keys:
                del self.keys[key]
                self.last = None
                return True
        return False

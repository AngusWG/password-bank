# password-bank

---

store/get password by command to your clipboard

## Features

---

- set account
- link key
- delete key
- Copy to clipboard
- Recent search priority

- [] file Encryption
- [] sync gist

## Example

* install 

```bash
> pip install git+https://github.com/AngusWG/password-bank.git
```

* store value

```bash
> pbank key account passwd
Are you sure to delete Account(account=account, password=passwd, keys=['key'])? (y/n) 
> y
Account(account=account, password=passwd, keys=['key'])
```

* get value to clipboard

```bash
> pbank key
Account(account=account, password=passwd, keys=['key'])
# your clipboard is 'account'

> pbank account 
Account(account=account, password=passwd, keys=['key'])
# your clipboard is 'passwd'
```

* find

```bash
> pbank key # or pbank account
Account(account=account, password=passwd, keys=['key'])

> pbank find key 
Account(account=account, password=passwd, keys=['key'])
Account(account=key, password=passwd, keys=['key_2'])

```

## Sync Config

github token gist key

---

* [Black formatter](https://github.com/psf/black)

> This project use black, please set `Continuation indent` = 4  
> Pycharm - File - Settings - Editor - Code Style - Python - Tabs and Indents

* [Flake8 lint](https://github.com/PyCQA/flake8)

> Use flake8 to check your code style.


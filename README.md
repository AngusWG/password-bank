# password-bank

--- 

store your password

* [Black formatter](https://github.com/psf/black)

> This project use black, please set `Continuation indent` = 4  
> Pycharm - File - Settings - Editor - Code Style - Python - Tabs and Indents

* [Flake8 lint](https://github.com/PyCQA/flake8)

> Use flake8 to check your code style.

* TODO

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

* store value

```bash
pbank key account passwd
> overwrite key-old-value?[y/n default:n]
y
key-value [id]
```

* find value

```bash
pbank key 
> email(on your copyboard) passwd

pbank email 
> passwd(on your copyboard) (by last search)
```

* find key

```bash
pbank find value

1 date key email passwd
2 date key email passwd
3 date key email passwd
```

* login

```bash
pbank login
github> token
gist> key
success
```

## Sync Config

github token gist key

# value-bank

--- 

store/get value by command to your clipboard

## Features

- set account
- link key
- delete key
- Copy to clipboard
- Recent search priority

- [ ] file Encryption
- [ ] sync gist
- [ ] re find

---

## Example

* install 

```bash
> pip install git+https://github.com/AngusWG/value-bank.git
```

* store value

```bash
vbank ubuntu root 123456
V(main_key=root, value=123456, ex_keys=['ubuntu'])
```

* get value to clipboard

```bash
vbank ubuntu
V(main_key=root, value=123456, ex_keys=['ubuntu'])
# your clipboard is 'root'


vbank root
V(main_key=root, value=123456, ex_keys=['ubuntu'])
# your clipboard is '123456' . Priority last record
```

* delete

```bash
vbank del ubuntu # or vbank del root
Are you sure to delete V(main_key=root, value=123456, ex_keys=['ubuntu'])? (y/n) y
vbank del
# None
```

* find

```bash
vbank find ubuntu
V(main_key=root, value=111111, ex_keys=['win'])
V(main_key=root, value=123123, ex_keys=['centos'])
```

## Sync Config

github token gist key

# todo

---

* [Black formatter](https://github.com/psf/black)

> This project use black, please set `Continuation indent` = 4  
> Pycharm - File - Settings - Editor - Code Style - Python - Tabs and Indents

* [Flake8 lint](https://github.com/PyCQA/flake8)

> Use flake8 to check your code style.
> 
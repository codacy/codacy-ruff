# hardcoded-password-default (S107)
Derived from the flake8-bandit linter.
## What it does
Checks for potential uses of hardcoded passwords in function argument
defaults.
## Why is this bad?
Including a hardcoded password in source code is a security risk, as an
attacker could discover the password and use it to gain unauthorized
access.
Instead, store passwords and other secrets in configuration files,
environment variables, or other sources that are excluded from version
control.
## Example
```
def connect_to_server(password="hunter2"): ...
```
## Use instead:
```
import os
def connect_to_server(password=os.environ["PASSWORD"]): ...
```
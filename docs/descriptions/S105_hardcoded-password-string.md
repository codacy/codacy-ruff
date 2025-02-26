# hardcoded-password-string (S105)
Derived from the flake8-bandit linter.
## What it does
Checks for potential uses of hardcoded passwords in strings.
## Why is this bad?
Including a hardcoded password in source code is a security risk, as an
attacker could discover the password and use it to gain unauthorized
access.
Instead, store passwords and other secrets in configuration files,
environment variables, or other sources that are excluded from version
control.
## Example
```
SECRET_KEY = "hunter2"
```
## Use instead:
```
import os
SECRET_KEY = os.environ["SECRET_KEY"]
```
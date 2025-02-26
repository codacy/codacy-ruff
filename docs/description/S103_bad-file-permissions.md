# bad-file-permissions (S103)
Derived from the flake8-bandit linter.
## What it does
Checks for files with overly permissive permissions.
## Why is this bad?
Overly permissive file permissions may allow unintended access and
arbitrary code execution.
## Example
```
import os
os.chmod("/etc/secrets.txt", 0o666)  # rw-rw-rw-
```
## Use instead:
```
import os
os.chmod("/etc/secrets.txt", 0o600)  # rw-------
```
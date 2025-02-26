# hardcoded-bind-all-interfaces (S104)
Derived from the flake8-bandit linter.
## What it does
Checks for hardcoded bindings to all network interfaces (0.0.0.0).
## Why is this bad?
Binding to all network interfaces is insecure as it allows access from
unintended interfaces, which may be poorly secured or unauthorized.
Instead, bind to specific interfaces.
## Example
```
ALLOWED_HOSTS = ["0.0.0.0"]
```
## Use instead:
```
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
```
# exec-builtin (S102)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the builtin exec function.
## Why is this bad?
The exec() function is insecure as it allows for arbitrary code
execution.
## Example
```
exec("print('Hello World')")
```
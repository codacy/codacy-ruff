# unused-function-argument (ARG001)
Derived from the flake8-unused-arguments linter.
## What it does
Checks for the presence of unused arguments in function definitions.
## Why is this bad?
An argument that is defined but not used is likely a mistake, and should
be removed to avoid confusion.
If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
lint.dummy-variable-rgx pattern.
## Example
```
def foo(bar, baz):
    return bar * 2
```
## Use instead:
```
def foo(bar):
    return bar * 2
```
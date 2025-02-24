# unused-method-argument (ARG002)
Derived from the flake8-unused-arguments linter.
## What it does
Checks for the presence of unused arguments in instance method definitions.
## Why is this bad?
An argument that is defined but not used is likely a mistake, and should
be removed to avoid confusion.
If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
lint.dummy-variable-rgx pattern.
## Example
```
class Class:
    def foo(self, arg1, arg2):
        print(arg1)
```
## Use instead:
```
class Class:
    def foo(self, arg1):
        print(arg1)
```
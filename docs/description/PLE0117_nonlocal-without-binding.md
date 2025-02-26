# nonlocal-without-binding (PLE0117)
Derived from the Pylint linter.
## What it does
Checks for nonlocal names without bindings.
## Why is this bad?
nonlocal names must be bound to a name in an outer scope.
Violating this rule leads to a SyntaxError at runtime.
## Example
```
def foo():
    def get_bar(self):
        nonlocal bar
        ...
```
## Use instead:
```
def foo():
    bar = 1
    def get_bar(self):
        nonlocal bar
        ...
```
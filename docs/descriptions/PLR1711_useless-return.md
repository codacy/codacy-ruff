# useless-return (PLR1711)
Derived from the Pylint linter.
Fix is always available.
## What it does
Checks for functions that end with an unnecessary return or
return None, and contain no other return statements.
## Why is this bad?
Python implicitly assumes a None return at the end of a function, making
it unnecessary to explicitly write return None.
## Example
```
def f():
    print(5)
    return None
```
## Use instead:
```
def f():
    print(5)
```
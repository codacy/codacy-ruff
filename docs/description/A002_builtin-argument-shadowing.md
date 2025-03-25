# builtin-argument-shadowing (A002)
Derived from the flake8-builtins linter.
## What it does
Checks for function arguments that use the same names as builtins.
## Why is this bad?
Reusing a builtin name for the name of an argument increases the
difficulty of reading and maintaining the code, and can cause
non-obvious errors, as readers may mistake the argument for the
builtin and vice versa.
Builtins can be marked as exceptions to this rule via the
lint.flake8-builtins.ignorelist configuration option.
## Example
```
def remove_duplicates(list, list2):
    result = set()
    for value in list:
        result.add(value)
    for value in list2:
        result.add(value)
    return list(result)  # TypeError: 'list' object is not callable
```
## Use instead:
```
def remove_duplicates(list1, list2):
    result = set()
    for value in list1:
        result.add(value)
    for value in list2:
        result.add(value)
    return list(result)
```
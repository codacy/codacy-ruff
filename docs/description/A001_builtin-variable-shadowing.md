# builtin-variable-shadowing (A001)
Derived from the flake8-builtins linter.
## What it does
Checks for variable (and function) assignments that use the same names
as builtins.
## Why is this bad?
Reusing a builtin name for the name of a variable increases the
difficulty of reading and maintaining the code, and can cause
non-obvious errors, as readers may mistake the variable for the
builtin and vice versa.
Builtins can be marked as exceptions to this rule via the
lint.flake8-builtins.ignorelist configuration option.
## Example
```
def find_max(list_of_lists):
    max = 0
    for flat_list in list_of_lists:
        for value in flat_list:
            max = max(max, value)  # TypeError: 'int' object is not callable
    return max
```
## Use instead:
```
def find_max(list_of_lists):
    result = 0
    for flat_list in list_of_lists:
        for value in flat_list:
            result = max(result, value)
    return result
```
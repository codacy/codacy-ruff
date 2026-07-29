# unmatched-suppression-comment (RUF104)
Added in 0.15.0 ·
Related issues ·
View source
## What it does
Checks for unmatched range suppression comments
## Why is this bad?
Unmatched range suppression comments can inadvertently suppress violations
over larger sections of code than intended, particularly at module scope.
## Example
```
def foo():
    # ruff: disable[E501]  # unmatched
    REALLY_LONG_VALUES = [...]
    print(REALLY_LONG_VALUES)
```
## Use instead:
```
def foo():
    # ruff: disable[E501]
    REALLY_LONG_VALUES = [...]
    # ruff: enable[E501]
    print(REALLY_LONG_VALUES)
```
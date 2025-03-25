# unnecessary-dict-comprehension-for-iterable (C420)
Derived from the flake8-comprehensions linter.
Fix is sometimes available.
## What it does
Checks for unnecessary dict comprehension when creating a dictionary from
an iterable.
## Why is this bad?
It's unnecessary to use a dict comprehension to build a dictionary from
an iterable when the value is static.
Prefer dict.fromkeys(iterable) over {value: None for value in iterable},
as dict.fromkeys is more readable and efficient.
## Example
```
{a: None for a in iterable}
{a: 1 for a in iterable}
```
## Use instead:
```
dict.fromkeys(iterable)
dict.fromkeys(iterable, 1)
```
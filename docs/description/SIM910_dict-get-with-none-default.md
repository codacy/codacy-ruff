# dict-get-with-none-default (SIM910)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for dict.get() calls that pass None as the default value.
## Why is this bad?
None is the default value for dict.get(), so it is redundant to pass it
explicitly.
## Example
```
ages = {"Tom": 23, "Maria": 23, "Dog": 11}
age = ages.get("Cat", None)
```
## Use instead:
```
ages = {"Tom": 23, "Maria": 23, "Dog": 11}
age = ages.get("Cat")
```
# static-key-dict-comprehension (B035)
Derived from the flake8-bugbear linter.
## What it does
Checks for dictionary comprehensions that use a static key, like a string
literal or a variable defined outside the comprehension.
## Why is this bad?
Using a static key (like a string literal) in a dictionary comprehension
is usually a mistake, as it will result in a dictionary with only one key,
despite the comprehension iterating over multiple values.
## Example
```
data = ["some", "Data"]
{"key": value.upper() for value in data}
```
## Use instead:
```
data = ["some", "Data"]
{value: value.upper() for value in data}
```
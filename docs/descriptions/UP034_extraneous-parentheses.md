# extraneous-parentheses (UP034)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for extraneous parentheses.
## Why is this bad?
Extraneous parentheses are redundant, and can be removed to improve
readability while retaining identical semantics.
## Example
```
print(("Hello, world"))
```
## Use instead:
```
print("Hello, world")
```
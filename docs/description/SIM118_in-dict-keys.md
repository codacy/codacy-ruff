# in-dict-keys (SIM118)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for key-existence checks against dict.keys() calls.
## Why is this bad?
When checking for the existence of a key in a given dictionary, using
key in dict is more readable and efficient than key in dict.keys(),
while having the same semantics.
## Example
```
key in foo.keys()
```
## Use instead:
```
key in foo
Fix safety
Given key in obj.keys(), obj could be a dictionary, or it could be
another type that defines a .keys() method. In the latter case, removing
the .keys() attribute could lead to a runtime error. The fix is marked
as safe when the type of obj is known to be a dictionary; otherwise, it
is marked as unsafe.
```
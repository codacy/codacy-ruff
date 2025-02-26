# duplicate-union-member (PYI016)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for duplicate union members.
## Why is this bad?
Duplicate union members are redundant and should be removed.
## Example
```
foo: str | str
```
## Use instead:
```
foo: str
Fix safety
This rule's fix is marked as safe unless the union contains comments.
For nested union, the fix will flatten type expressions into a single
top-level union.
```
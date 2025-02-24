# unnecessary-type-union (PYI055)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for the presence of multiple types in a union.
## Why is this bad?
type[T | S] has identical semantics to type[T] | type[S] in a type
annotation, but is cleaner and more concise.
## Example
```
field: type[int] | type[float] | str
```
## Use instead:
```
field: type[int | float] | str
Fix safety
This rule's fix is marked as safe, unless the type annotation contains comments.
Note that while the fix may flatten nested unions into a single top-level union,
the semantics of the annotation will remain unchanged.
```
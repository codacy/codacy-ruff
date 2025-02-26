# get-attr-with-constant (B009)
Derived from the flake8-bugbear linter.
Fix is always available.
## What it does
Checks for uses of getattr that take a constant attribute value as an
argument (e.g., getattr(obj, "foo")).
## Why is this bad?
getattr is used to access attributes dynamically. If the attribute is
defined as a constant, it is no safer than a typical property access. When
possible, prefer property access over getattr calls, as the former is
more concise and idiomatic.
## Example
```
getattr(obj, "foo")
```
## Use instead:
```
obj.foo
```
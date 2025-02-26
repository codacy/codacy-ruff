# set-attr-with-constant (B010)
Derived from the flake8-bugbear linter.
Fix is always available.
## What it does
Checks for uses of setattr that take a constant attribute value as an
argument (e.g., setattr(obj, "foo", 42)).
## Why is this bad?
setattr is used to set attributes dynamically. If the attribute is
defined as a constant, it is no safer than a typical property access. When
possible, prefer property access over setattr calls, as the former is
more concise and idiomatic.
## Example
```
setattr(obj, "foo", 42)
```
## Use instead:
```
obj.foo = 42
```
# raise-literal (B016)
Added in v0.0.102 ·
Related issues ·
View source
Derived from the flake8-bugbear linter.
## What it does
Checks for raise statements that raise a literal value.
## Why is this bad?
raise must be followed by an exception instance or an exception class,
and exceptions must be instances of BaseException or a subclass thereof.
Raising a literal will raise a TypeError at runtime.
## Example
```
raise "foo"
```
## Use instead:
```
raise Exception("foo")
```
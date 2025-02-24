# if-else-block-instead-of-dict-get (SIM401)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for if statements that can be replaced with dict.get calls.
## Why is this bad?
dict.get() calls can be used to replace if statements that assign a
value to a variable in both branches, falling back to a default value if
the key is not found. When possible, using dict.get is more concise and
more idiomatic.
Under preview mode, this rule will
also suggest replacing if-else expressions with dict.get calls.
## Example
```
if "bar" in foo:
    value = foo["bar"]
else:
    value = 0
```
## Use instead:
```
value = foo.get("bar", 0)
If preview mode is enabled:
value = foo["bar"] if "bar" in foo else 0
```
## Use instead:
```
value = foo.get("bar", 0)
```
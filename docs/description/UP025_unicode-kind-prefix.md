# unicode-kind-prefix (UP025)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of the Unicode kind prefix (u) in strings.
## Why is this bad?
In Python 3, all strings are Unicode by default. The Unicode kind prefix is
unnecessary and should be removed to avoid confusion.
## Example
```
u"foo"
```
## Use instead:
```
"foo"
```
# blank-line-with-whitespace (W293)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for superfluous whitespace in blank lines.
## Why is this bad?
According to PEP 8, "avoid trailing whitespace anywhere. Because it’s usually
invisible, it can be confusing"
## Example
```
class Foo(object):\n    \n    bang = 12
```
## Use instead:
```
class Foo(object):\n\n    bang = 12
```
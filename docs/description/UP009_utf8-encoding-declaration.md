# utf8-encoding-declaration (UP009)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary UTF-8 encoding declarations.
## Why is this bad?
PEP 3120 makes UTF-8 the default encoding, so a UTF-8 encoding
declaration is unnecessary.
## Example
```
# -*- coding: utf-8 -*-
print("Hello, world!")
```
## Use instead:
```
print("Hello, world!")
```
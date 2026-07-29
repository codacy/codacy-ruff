# multiple-imports-on-one-line (E401)
Added in v0.0.191 ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Check for multiple imports on one line.
## Why is this bad?
According to PEP 8, "imports should usually be on separate lines."
## Example
```
import sys, os
```
## Use instead:
```
import os
import sys
```
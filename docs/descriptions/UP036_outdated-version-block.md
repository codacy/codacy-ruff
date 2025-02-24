# outdated-version-block (UP036)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for conditional blocks gated on sys.version_info comparisons
that are outdated for the minimum supported Python version.
## Why is this bad?
In Python, code can be conditionally executed based on the active
Python version by comparing against the sys.version_info tuple.
If a code block is only executed for Python versions older than the
minimum supported version, it should be removed.
## Example
```
import sys
if sys.version_info < (3, 0):
    print("py2")
else:
    print("py3")
```
## Use instead:
```
print("py3")
```
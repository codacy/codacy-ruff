# sys-version-info0-eq3 (YTT201)
Derived from the flake8-2020 linter.
## What it does
Checks for equality comparisons against the major version returned by
sys.version_info (e.g., sys.version_info[0] == 3).
## Why is this bad?
Using sys.version_info[0] == 3 to verify that the major version is
Python 3 or greater will fail if the major version number is ever
incremented (e.g., to Python 4). This is likely unintended, as code
that uses this comparison is likely intended to be run on Python 2,
but would now run on Python 4 too.
Instead, use >= to check if the major version number is 3 or greater,
to future-proof the code.
## Example
```
import sys
if sys.version_info[0] == 3:
    ...
else:
    print("Python 2")  # This will be printed on Python 4.
```
## Use instead:
```
import sys
if sys.version_info >= (3,):
    ...
else:
    print("Python 2")  # This will not be printed on Python 4.
```
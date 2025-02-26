# bad-version-info-comparison (PYI006)
Derived from the flake8-pyi linter.
## What it does
Checks for uses of comparators other than < and >= for
sys.version_info checks. All other comparators, such
as >, <=, and ==, are banned.
## Why is this bad?
Comparing sys.version_info with == or <= has unexpected behavior
and can lead to bugs.
For example, sys.version_info > (3, 8, 1) will resolve to True if your
Python version is 3.8.1; meanwhile, sys.version_info <= (3, 8) will not
resolve to True if your Python version is 3.8.10:
>>> import sys
>>> print(sys.version_info)
sys.version_info(major=3, minor=8, micro=10, releaselevel='final', serial=0)
>>> print(sys.version_info > (3, 8))
True
>>> print(sys.version_info == (3, 8))
False
>>> print(sys.version_info <= (3, 8))
False
>>> print(sys.version_info in (3, 8))
False
## Example
```
import sys
if sys.version_info > (3, 8): ...
```
## Use instead:
```
import sys
if sys.version_info >= (3, 9): ...
```
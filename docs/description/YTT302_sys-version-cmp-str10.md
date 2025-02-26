# sys-version-cmp-str10 (YTT302)
Derived from the flake8-2020 linter.
## What it does
Checks for comparisons that test sys.version against string literals,
such that the comparison would fail if the major version number were
ever incremented to Python 10 or higher.
## Why is this bad?
Comparing sys.version to a string is error-prone and may cause subtle
bugs, as the comparison will be performed lexicographically, not
semantically.
Instead, use sys.version_info to access the current major and minor
version numbers as a tuple, which can be compared to other tuples
without issue.
## Example
```
import sys
sys.version >= "3"  # `False` on Python 10.
```
## Use instead:
```
import sys
sys.version_info >= (3,)  # `True` on Python 10.
```
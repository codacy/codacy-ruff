# sys-version-info1-cmp-int (YTT203)
Derived from the flake8-2020 linter.
## What it does
Checks for comparisons that test sys.version_info[1] against an integer.
## Why is this bad?
Comparisons based on the current minor version number alone can cause
subtle bugs and would likely lead to unintended effects if the Python
major version number were ever incremented (e.g., to Python 4).
Instead, compare sys.version_info to a tuple, including the major and
minor version numbers, to future-proof the code.
## Example
```
import sys
if sys.version_info[1] < 7:
    print("Python 3.6 or earlier.")  # This will be printed on Python 4.0.
```
## Use instead:
```
import sys
if sys.version_info < (3, 7):
    print("Python 3.6 or earlier.")
```
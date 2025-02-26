# deprecated-import (UP035)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for uses of deprecated imports based on the minimum supported
Python version.
## Why is this bad?
Deprecated imports may be removed in future versions of Python, and
should be replaced with their new equivalents.
Note that, in some cases, it may be preferable to continue importing
members from typing_extensions even after they're added to the Python
standard library, as typing_extensions can backport bugfixes and
optimizations from later Python versions. This rule thus avoids flagging
imports from typing_extensions in such cases.
## Example
```
from collections import Sequence
```
## Use instead:
```
from collections.abc import Sequence
```
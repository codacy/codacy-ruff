# deprecated-mock-import (UP026)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for imports of the mock module that should be replaced with
unittest.mock.
## Why is this bad?
Since Python 3.3, mock has been a part of the standard library as
unittest.mock. The mock package is deprecated; use unittest.mock
instead.
## Example
```
import mock
```
## Use instead:
```
from unittest import mock
```
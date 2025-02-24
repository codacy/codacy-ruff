# pytest-incorrect-pytest-import (PT013)
Derived from the flake8-pytest-style linter.
## What it does
Checks for incorrect import of pytest.
## Why is this bad?
For consistency, pytest should be imported as import pytest and its members should be
accessed in the form of pytest.xxx.yyy for consistency
## Example
```
import pytest as pt
from pytest import fixture
```
## Use instead:
```
import pytest
```
# pytest-erroneous-use-fixtures-on-fixture (PT025)
Derived from the flake8-pytest-style linter.
Fix is always available.
## What it does
Checks for pytest.mark.usefixtures decorators applied to pytest
fixtures.
## Why is this bad?
The pytest.mark.usefixtures decorator has no effect on pytest fixtures.
## Example
```
import pytest
@pytest.fixture()
def a():
    pass
@pytest.mark.usefixtures("a")
@pytest.fixture()
def b(a):
    pass
```
## Use instead:
```
import pytest
@pytest.fixture()
def a():
    pass
@pytest.fixture()
def b(a):
    pass
```
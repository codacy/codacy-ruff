# pytest-extraneous-scope-function (PT003)
Added in v0.0.208 ·
Related issues ·
View source
Derived from the flake8-pytest-style linter.
Fix is always available.
## What it does
Checks for pytest.fixture calls with scope="function".
## Why is this bad?
scope="function" can be omitted, as it is the default.
## Example
```
import pytest
@pytest.fixture(scope="function")
def my_fixture(): ...
```
## Use instead:
```
import pytest
@pytest.fixture()
def my_fixture(): ...
```
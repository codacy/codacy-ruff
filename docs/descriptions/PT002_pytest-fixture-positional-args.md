# pytest-fixture-positional-args (PT002)
Derived from the flake8-pytest-style linter.
## What it does
Checks for pytest.fixture calls with positional arguments.
## Why is this bad?
For clarity and consistency, prefer using keyword arguments to specify
fixture configuration.
## Example
```
import pytest
@pytest.fixture("module")
def my_fixture(): ...
```
## Use instead:
```
import pytest
@pytest.fixture(scope="module")
def my_fixture(): ...
```
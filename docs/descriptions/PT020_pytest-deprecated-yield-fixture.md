# pytest-deprecated-yield-fixture (PT020)
Derived from the flake8-pytest-style linter.
## What it does
Checks for pytest.yield_fixture usage.
## Why is this bad?
pytest.yield_fixture is deprecated. pytest.fixture should be used instead.
## Example
```
import pytest
@pytest.yield_fixture()
def my_fixture():
    obj = SomeClass()
    yield obj
    obj.cleanup()
```
## Use instead:
```
import pytest
@pytest.fixture()
def my_fixture():
    obj = SomeClass()
    yield obj
    obj.cleanup()
```
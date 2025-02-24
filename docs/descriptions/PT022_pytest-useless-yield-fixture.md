# pytest-useless-yield-fixture (PT022)
Derived from the flake8-pytest-style linter.
Fix is always available.
## What it does
Checks for unnecessary yield expressions in pytest fixtures.
## Why is this bad?
In pytest fixtures, the yield expression should only be used for fixtures
that include teardown code, to clean up the fixture after the test function
has finished executing.
## Example
```
import pytest
@pytest.fixture()
def my_fixture():
    resource = acquire_resource()
    yield resource
```
## Use instead:
```
import pytest
@pytest.fixture()
def my_fixture_with_teardown():
    resource = acquire_resource()
    yield resource
    resource.release()
@pytest.fixture()
def my_fixture_without_teardown():
    resource = acquire_resource()
    return resource
```
# pytest-fixture-finalizer-callback (PT021)
Derived from the flake8-pytest-style linter.
## What it does
Checks for unnecessary request.addfinalizer usages in pytest fixtures.
## Why is this bad?
pytest offers two ways to perform cleanup in fixture code. The first is
sequential (via the yield statement), the second callback-based (via
request.addfinalizer).
The sequential approach is more readable and should be preferred, unless
the fixture uses the "factory as fixture" pattern.
## Example
```
import pytest
@pytest.fixture()
def my_fixture(request):
    resource = acquire_resource()
    request.addfinalizer(resource.release)
    return resource
```
## Use instead:
```
import pytest
@pytest.fixture()
def my_fixture():
    resource = acquire_resource()
    yield resource
    resource.release()
# "factory-as-fixture" pattern
@pytest.fixture()
def my_factory(request):
    def create_resource(arg):
        resource = acquire_resource(arg)
        request.addfinalizer(resource.release)
        return resource
    return create_resource
```
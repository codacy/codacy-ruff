# pytest-fixture-param-without-value (PT019)
Derived from the flake8-pytest-style linter.
## What it does
Checks for pytest test functions that should be decorated with
@pytest.mark.usefixtures.
## Why is this bad?
In pytest, fixture injection is used to activate fixtures in a test
function.
Fixtures can be injected either by passing them as parameters to the test
function, or by using the @pytest.mark.usefixtures decorator.
If the test function depends on the fixture being activated, but does not
use it in the test body or otherwise rely on its return value, prefer
the @pytest.mark.usefixtures decorator, to make the dependency explicit
and avoid the confusion caused by unused arguments.
## Example
```
import pytest
@pytest.fixture
def _patch_something(): ...
def test_foo(_patch_something): ...
```
## Use instead:
```
import pytest
@pytest.fixture
def _patch_something(): ...
@pytest.mark.usefixtures("_patch_something")
def test_foo(): ...
```
# pytest-deprecated-yield-fixture (PT020)
Added in v0.0.208 ·
Related issues ·
View source
Derived from the flake8-pytest-style linter.
Fix is sometimes available.
## What it does
Checks for pytest.yield_fixture usage.
## Why is this bad?
pytest.fixture has supported yield since pytest 3.0, which left
pytest.yield_fixture as a plain alias for it. The alias has been
deprecated since pytest 6.2, now raises a PytestRemovedIn10Warning, and
will be removed in pytest 10.
The two are the same function, so switching to pytest.fixture is a
rename with no other consequence.
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
Fix safety
This rule's fix is marked as safe, unless the decorator contains comments
that the fix would remove. pytest.yield_fixture and pytest.fixture are
the same function; the only behavioral difference is the deprecation
warning that pytest.yield_fixture emits.
```
# pytest-assert-always-false (PT015)
Derived from the flake8-pytest-style linter.
## What it does
Checks for assert statements whose test expression is a falsy value.
## Why is this bad?
pytest.fail conveys the intent more clearly than assert falsy_value.
## Example
```
def test_foo():
    if some_condition:
        assert False, "some_condition was True"
```
## Use instead:
```
import pytest
def test_foo():
    if some_condition:
        pytest.fail("some_condition was True")
    ...
```
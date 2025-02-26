# pytest-raises-without-exception (PT010)
Derived from the flake8-pytest-style linter.
## What it does
Checks for pytest.raises calls without an expected exception.
## Why is this bad?
pytest.raises expects to receive an expected exception as its first
argument. If omitted, the pytest.raises call will fail at runtime.
## Example
```
import pytest
def test_foo():
    with pytest.raises():
        do_something()
```
## Use instead:
```
import pytest
def test_foo():
    with pytest.raises(SomeException):
        do_something()
```
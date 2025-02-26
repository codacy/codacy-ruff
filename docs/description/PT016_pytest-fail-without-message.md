# pytest-fail-without-message (PT016)
Derived from the flake8-pytest-style linter.
## What it does
Checks for pytest.fail calls without a message.
## Why is this bad?
pytest.fail calls without a message make it harder to understand and debug test failures.
## Example
```
import pytest
def test_foo():
    pytest.fail()
def test_bar():
    pytest.fail("")
def test_baz():
    pytest.fail(reason="")
```
## Use instead:
```
import pytest
def test_foo():
    pytest.fail("...")
def test_bar():
    pytest.fail(reason="...")
```
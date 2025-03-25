# pytest-raises-with-multiple-statements (PT012)
Derived from the flake8-pytest-style linter.
## What it does
Checks for pytest.raises context managers with multiple statements.
This rule allows pytest.raises bodies to contain for
loops with empty bodies (e.g., pass or ... statements), to test
iterator behavior.
## Why is this bad?
When a pytest.raises is used as a context manager and contains multiple
statements, it can lead to the test passing when it actually should fail.
A pytest.raises context manager should only contain a single simple
statement that raises the expected exception.
## Example
```
import pytest
def test_foo():
    with pytest.raises(MyError):
        setup()
        func_to_test()  # not executed if `setup()` raises `MyError`
        assert foo()  # not executed
```
## Use instead:
```
import pytest
def test_foo():
    setup()
    with pytest.raises(MyError):
        func_to_test()
    assert foo()
```
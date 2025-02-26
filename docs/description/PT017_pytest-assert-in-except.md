# pytest-assert-in-except (PT017)
Derived from the flake8-pytest-style linter.
## What it does
Checks for assert statements in except clauses.
## Why is this bad?
When testing for exceptions, pytest.raises() should be used instead of
assert statements in except clauses, as it's more explicit and
idiomatic. Further, pytest.raises() will fail if the exception is not
raised, unlike the assert statement.
## Example
```
def test_foo():
    try:
        1 / 0
    except ZeroDivisionError as e:
        assert e.args
```
## Use instead:
```
import pytest
def test_foo():
    with pytest.raises(ZeroDivisionError) as exc_info:
        1 / 0
    assert exc_info.value.args
```
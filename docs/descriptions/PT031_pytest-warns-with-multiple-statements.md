# pytest-warns-with-multiple-statements (PT031)
Derived from the flake8-pytest-style linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for pytest.warns context managers with multiple statements.
## Why is this bad?
When pytest.warns is used as a context manager and contains multiple
statements, it can lead to the test passing when it should instead fail.
A pytest.warns context manager should only contain a single
simple statement that triggers the expected warning.
In preview, this rule allows pytest.warns bodies to contain for
loops with empty bodies (e.g., pass or ... statements), to test
iterator behavior.
## Example
```
import pytest
def test_foo_warns():
    with pytest.warns(Warning):
        setup()  # False negative if setup triggers a warning but foo does not.
        foo()
```
## Use instead:
```
import pytest
def test_foo_warns():
    setup()
    with pytest.warns(Warning):
        foo()
```
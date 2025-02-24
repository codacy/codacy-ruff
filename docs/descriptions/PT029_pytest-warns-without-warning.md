# pytest-warns-without-warning (PT029)
Derived from the flake8-pytest-style linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for pytest.warns calls without an expected warning.
## Why is this bad?
pytest.warns expects to receive an expected warning as its first
argument. If omitted, the pytest.warns call will fail at runtime.
## Example
```
import pytest
def test_foo():
    with pytest.warns():
        do_something()
```
## Use instead:
```
import pytest
def test_foo():
    with pytest.warns(SomeWarning):
        do_something()
```
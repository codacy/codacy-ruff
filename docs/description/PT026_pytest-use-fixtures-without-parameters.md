# pytest-use-fixtures-without-parameters (PT026)
Derived from the flake8-pytest-style linter.
Fix is always available.
## What it does
Checks for @pytest.mark.usefixtures() decorators that aren't passed any
arguments.
## Why is this bad?
A @pytest.mark.usefixtures() decorator that isn't passed any arguments is
useless and should be removed.
## Example
```
import pytest
@pytest.mark.usefixtures()
def test_something(): ...
```
## Use instead:
```
def test_something(): ...
```
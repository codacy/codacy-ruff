# pytest-incorrect-mark-parentheses-style (PT023)
Derived from the flake8-pytest-style linter.
Fix is always available.
## What it does
Checks for argument-free @pytest.mark.<marker>() decorators with or
without parentheses, depending on the lint.flake8-pytest-style.mark-parentheses
setting.
The rule defaults to removing unnecessary parentheses,
to match the documentation of the official pytest projects.
## Why is this bad?
If a @pytest.mark.<marker>() doesn't take any arguments, the parentheses are
optional.
Either removing those unnecessary parentheses or requiring them for all
fixtures is fine, but it's best to be consistent.
## Example
```
import pytest
@pytest.mark.foo
def test_something(): ...
```
## Use instead:
```
import pytest
@pytest.mark.foo()
def test_something(): ...
```
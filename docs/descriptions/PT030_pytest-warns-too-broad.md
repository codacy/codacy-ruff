# pytest-warns-too-broad (PT030)
Derived from the flake8-pytest-style linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for pytest.warns calls without a match parameter.
## Why is this bad?
pytest.warns(Warning) will catch any Warning and may catch warnings that
are unrelated to the code under test. To avoid this, pytest.warns should
be called with a match parameter. The warning names that require a match
parameter can be configured via the
lint.flake8-pytest-style.warns-require-match-for and
lint.flake8-pytest-style.warns-extend-require-match-for settings.
## Example
```
import pytest
def test_foo():
    with pytest.warns(RuntimeWarning):
        ...
    # empty string is also an error
    with pytest.warns(RuntimeWarning, match=""):
        ...
```
## Use instead:
```
import pytest
def test_foo():
    with pytest.warns(RuntimeWarning, match="expected message"):
        ...
```
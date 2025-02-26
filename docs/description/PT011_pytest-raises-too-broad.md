# pytest-raises-too-broad (PT011)
Derived from the flake8-pytest-style linter.
## What it does
Checks for pytest.raises calls without a match parameter.
## Why is this bad?
pytest.raises(Error) will catch any Error and may catch errors that are
unrelated to the code under test. To avoid this, pytest.raises should be
called with a match parameter. The exception names that require a match
parameter can be configured via the
lint.flake8-pytest-style.raises-require-match-for and
lint.flake8-pytest-style.raises-extend-require-match-for settings.
## Example
```
import pytest
def test_foo():
    with pytest.raises(ValueError):
        ...
    # empty string is also an error
    with pytest.raises(ValueError, match=""):
        ...
```
## Use instead:
```
import pytest
def test_foo():
    with pytest.raises(ValueError, match="expected message"):
        ...
```
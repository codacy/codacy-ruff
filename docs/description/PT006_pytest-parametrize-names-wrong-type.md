# pytest-parametrize-names-wrong-type (PT006)
Derived from the flake8-pytest-style linter.
Fix is sometimes available.
## What it does
Checks for the type of parameter names passed to pytest.mark.parametrize.
## Why is this bad?
The argnames argument of pytest.mark.parametrize takes a string or
a sequence of strings. For a single parameter, it's preferable to use a
string. For multiple parameters, it's preferable to use the style
configured via the lint.flake8-pytest-style.parametrize-names-type setting.
## Example
```
import pytest
# single parameter, always expecting string
@pytest.mark.parametrize(("param",), [1, 2, 3])
def test_foo(param): ...
# multiple parameters, expecting tuple
@pytest.mark.parametrize(["param1", "param2"], [(1, 2), (3, 4)])
def test_bar(param1, param2): ...
# multiple parameters, expecting tuple
@pytest.mark.parametrize("param1,param2", [(1, 2), (3, 4)])
def test_baz(param1, param2): ...
```
## Use instead:
```
import pytest
@pytest.mark.parametrize("param", [1, 2, 3])
def test_foo(param): ...
@pytest.mark.parametrize(("param1", "param2"), [(1, 2), (3, 4)])
def test_bar(param1, param2): ...
```
# pytest-fixture-incorrect-parentheses-style (PT001)
Derived from the flake8-pytest-style linter.
Fix is always available.
## What it does
Checks for argument-free @pytest.fixture() decorators with or without
parentheses, depending on the lint.flake8-pytest-style.fixture-parentheses
setting.
## Why is this bad?
If a @pytest.fixture() doesn't take any arguments, the parentheses are
optional.
Either removing those unnecessary parentheses or requiring them for all
fixtures is fine, but it's best to be consistent. The rule defaults to
removing unnecessary parentheses, to match the documentation of the
official pytest projects.
## Example
```
import pytest
@pytest.fixture()
def my_fixture(): ...
```
## Use instead:
```
import pytest
@pytest.fixture
def my_fixture(): ...
Fix safety
This rule's fix is marked as unsafe if there's comments in the
pytest.fixture decorator.
For example, the fix would be marked as unsafe in the following case:
import pytest
@pytest.fixture(
    # comment
    # scope = "module"
)
def my_fixture(): ...
```
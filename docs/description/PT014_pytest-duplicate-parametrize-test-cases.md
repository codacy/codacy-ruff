# pytest-duplicate-parametrize-test-cases (PT014)
Derived from the flake8-pytest-style linter.
Fix is sometimes available.
## What it does
Checks for duplicate test cases in pytest.mark.parametrize.
## Why is this bad?
Duplicate test cases are redundant and should be removed.
## Example
```
import pytest
@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        (1, 2),
        (1, 2),
    ],
)
def test_foo(param1, param2): ...
```
## Use instead:
```
import pytest
@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        (1, 2),
    ],
)
def test_foo(param1, param2): ...
Fix safety
This rule's fix is marked as unsafe, as tests that rely on mutable global
state may be affected by removing duplicate test cases.
```
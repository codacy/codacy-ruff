# pytest-composite-assertion (PT018)
Derived from the flake8-pytest-style linter.
Fix is sometimes available.
## What it does
Checks for assertions that combine multiple independent conditions.
## Why is this bad?
Composite assertion statements are harder to debug upon failure, as the
failure message will not indicate which condition failed.
## Example
```
def test_foo():
    assert something and something_else
def test_bar():
    assert not (something or something_else)
```
## Use instead:
```
def test_foo():
    assert something
    assert something_else
def test_bar():
    assert not something
    assert not something_else
```
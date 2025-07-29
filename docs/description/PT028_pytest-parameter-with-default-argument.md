# pytest-parameter-with-default-argument (PT028)
Derived from the flake8-pytest-style linter.
## What it does
Checks for parameters of test functions with default arguments.
## Why is this bad?
Such a parameter will always have the default value during the test
regardless of whether a fixture with the same name is defined.
## Example
```
def test_foo(a=1): ...
```
## Use instead:
```
def test_foo(a): ...
Fix safety
This rule's fix is marked as unsafe, as modifying a function signature can
change the behavior of the code.
```
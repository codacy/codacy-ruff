# pytest-unittest-raises-assertion (PT027)
Derived from the flake8-pytest-style linter.
Fix is sometimes available.
## What it does
Checks for uses of exception-related assertion methods from the unittest
module.
## Why is this bad?
To enforce the assertion style recommended by pytest, pytest.raises is
preferred over the exception-related assertion methods in unittest, like
assertRaises.
## Example
```
import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        with self.assertRaises(ValueError):
            raise ValueError("foo")
```
## Use instead:
```
import unittest
import pytest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        with pytest.raises(ValueError):
            raise ValueError("foo")
```
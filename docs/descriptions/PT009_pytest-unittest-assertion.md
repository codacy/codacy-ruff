# pytest-unittest-assertion (PT009)
Derived from the flake8-pytest-style linter.
Fix is sometimes available.
## What it does
Checks for uses of assertion methods from the unittest module.
## Why is this bad?
To make use of pytest's assertion rewriting, a regular assert statement
is preferred over unittest's assertion methods.
## Example
```
import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(a, b)
```
## Use instead:
```
import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        assert a == b
```
# deprecated-unittest-alias (UP005)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of deprecated methods from the unittest module.
## Why is this bad?
The unittest module has deprecated aliases for some of its methods.
The deprecated aliases were removed in Python 3.12. Instead of aliases,
use their non-deprecated counterparts.
## Example
```
from unittest import TestCase
class SomeTest(TestCase):
    def test_something(self):
        self.assertEquals(1, 1)
```
## Use instead:
```
from unittest import TestCase
class SomeTest(TestCase):
    def test_something(self):
        self.assertEqual(1, 1)
```
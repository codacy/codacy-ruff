# self-or-cls-assignment (PLW0642)
Derived from the Pylint linter.
## What it does
Checks for assignment of self and cls in instance and class methods respectively.
This check also applies to __new__ even though this is technically
a static method.
## Why is this bad?
The identifiers self and cls are conventional in Python for the first parameter of instance
methods and class methods, respectively. Assigning new values to these variables can be
confusing for others reading your code; using a different variable name can lead to clearer
code.
## Example
```
class Version:
    def add(self, other):
        self = self + other
        return self
    @classmethod
    def superclass(cls):
        cls = cls.__mro__[-1]
        return cls
```
## Use instead:
```
class Version:
    def add(self, other):
        new_version = self + other
        return new_version
    @classmethod
    def superclass(cls):
        supercls = cls.__mro__[-1]
        return supercls
```
# collections-named-tuple (PYI024)
Derived from the flake8-pyi linter.
## What it does
Checks for uses of collections.namedtuple in stub files.
## Why is this bad?
typing.NamedTuple is the "typed version" of collections.namedtuple.
Inheriting from typing.NamedTuple creates a custom tuple subclass in
the same way as using the collections.namedtuple factory function.
However, using typing.NamedTuple allows you to provide a type annotation
for each field in the class. This means that type checkers will have more
information to work with, and will be able to analyze your code more
precisely.
## Example
```
from collections import namedtuple
person = namedtuple("Person", ["name", "age"])
```
## Use instead:
```
from typing import NamedTuple
class Person(NamedTuple):
    name: str
    age: int
```
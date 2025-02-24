# class-as-data-structure (B903)
Derived from the flake8-bugbear linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for classes that only have a public __init__ method,
without base classes and decorators.
## Why is this bad?
Classes with just an __init__ are possibly better off
being a dataclass or a namedtuple, which have less boilerplate.
## Example
```
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
```
## Use instead:
```
from dataclasses import dataclass
@dataclass
class Point:
    x: float
    y: float
```
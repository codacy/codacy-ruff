# empty-method-without-abstract-decorator (B027)
Derived from the flake8-bugbear linter.
## What it does
Checks for empty methods in abstract base classes without an abstract
decorator.
## Why is this bad?
Empty methods in abstract base classes without an abstract decorator may be
be indicative of a mistake. If the method is meant to be abstract, add an
@abstractmethod decorator to the method.
## Example
```
from abc import ABC
class Foo(ABC):
    def method(self): ...
```
## Use instead:
```
from abc import ABC, abstractmethod
class Foo(ABC):
    @abstractmethod
    def method(self): ...
```
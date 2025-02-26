# abstract-base-class-without-abstract-method (B024)
Derived from the flake8-bugbear linter.
## What it does
Checks for abstract classes without abstract methods or properties.
Annotated but unassigned class variables are regarded as abstract.
## Why is this bad?
Abstract base classes are used to define interfaces. If an abstract base
class has no abstract methods or properties, you may have forgotten
to add an abstract method or property to the class,
or omitted an @abstractmethod decorator.
If the class is not meant to be used as an interface, consider removing
the ABC base class from the class definition.
## Example
```
from abc import ABC
from typing import ClassVar
class Foo(ABC):
    class_var: ClassVar[str] = "assigned"
    def method(self):
        bar()
```
## Use instead:
```
from abc import ABC, abstractmethod
from typing import ClassVar
class Foo(ABC):
    class_var: ClassVar[str]  # unassigned
    @abstractmethod
    def method(self):
        bar()
```
# incorrect-decorator-order (RUF074)
Preview (since 0.15.14) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for incorrect ordering of decorators on functions and methods.
## Why is this bad?
Decorators are applied bottom-up. Certain decorator combinations cause
runtime errors or silent wrong behavior when placed in the wrong order.
For example, @abstractmethod must be the innermost (bottom) decorator
when combined with @property, @classmethod, or @staticmethod.
## Example
```
from abc import abstractmethod
class Foo:
    @abstractmethod
    @property
    def bar(self): ...
```
## Use instead:
```
from abc import abstractmethod
class Foo:
    @property
    @abstractmethod
    def bar(self): ...
```
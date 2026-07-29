# deprecated-abc-decorator (UP051)
Preview (since 0.15.21) ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of abstractclassmethod, abstractstaticmethod, abstractproperty.
## Why is this bad?
These have been deprecated since Python 3.3 and are expected to be removed in a future version
of Python.
## Example
```
import abc
class Foo(abc.ABC):
    @abc.abstractclassmethod
    def class_method(cls, arg1): ...
    @abc.abstractstaticmethod
    def static_method(arg1): ...
    @abc.abstractproperty
    def prop(self): ...
```
## Use instead:
```
import abc
class Foo(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def class_method(cls, arg1): ...
    @staticmethod
    @abc.abstractmethod
    def static_method(arg1): ...
    @property
    @abc.abstractmethod
    def prop(self): ...
```
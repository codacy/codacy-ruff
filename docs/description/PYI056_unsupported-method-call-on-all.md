# unsupported-method-call-on-all (PYI056)
Derived from the flake8-pyi linter.
## What it does
Checks that append, extend and remove methods are not called on
__all__.
## Why is this bad?
Different type checkers have varying levels of support for calling these
methods on __all__. Instead, use the += operator to add items to
__all__, which is known to be supported by all major type checkers.
## Example
```
import sys
__all__ = ["A", "B"]
if sys.version_info >= (3, 10):
    __all__.append("C")
if sys.version_info >= (3, 11):
    __all__.remove("B")
```
## Use instead:
```
import sys
__all__ = ["A"]
if sys.version_info < (3, 11):
    __all__ += ["B"]
if sys.version_info >= (3, 10):
    __all__ += ["C"]
```
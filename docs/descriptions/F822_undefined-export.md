# undefined-export (F822)
Derived from the Pyflakes linter.
## What it does
Checks for undefined names in __all__.
## Why is this bad?
In Python, the __all__ variable is used to define the names that are
exported when a module is imported as a wildcard (e.g.,
from foo import *). The names in __all__ must be defined in the module,
but are included as strings.
Including an undefined name in __all__ is likely to raise NameError at
runtime, when the module is imported.
In preview, this rule will flag undefined names in __init__.py file,
even if those names implicitly refer to other modules in the package. Users
that rely on implicit exports should disable this rule in __init__.py
files via lint.per-file-ignores.
## Example
```
from foo import bar
__all__ = ["bar", "baz"]  # undefined name `baz` in `__all__`
```
## Use instead:
```
from foo import bar, baz
__all__ = ["bar", "baz"]
```
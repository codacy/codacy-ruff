# non-empty-init-module (RUF067)
Preview (since 0.14.11) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Detects the presence of code in __init__.py files.
## Why is this bad?
__init__.py files are often empty or only contain simple code to modify a module's API. As
such, it's easy to overlook them and their possible side effects when debugging.
## Example
```
Instead of defining MyClass directly in __init__.py:
"""My module docstring."""
class MyClass:
    def my_method(self): ...
move the definition to another file, import it, and include it in __all__:
"""My module docstring."""
from submodule import MyClass
__all__ = ["MyClass"]
Code in __init__.py files is also run at import time and can cause surprising slowdowns. To
disallow any code in __init__.py files, you can enable the
lint.ruff.strictly-empty-init-modules setting. In this case:
from submodule import MyClass
__all__ = ["MyClass"]
the only fix is entirely emptying the file:
Details
In non-strict mode, this rule allows several common patterns in __init__.py files:
Imports
Assignments to dunder names (identifiers starting and ending with __, such as __all__ or
    __submodules__)
Module-level and attribute docstrings
if TYPE_CHECKING blocks
PEP-562 module-level __getattr__ and __dir__ functions
```
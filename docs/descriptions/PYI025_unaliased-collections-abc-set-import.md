# unaliased-collections-abc-set-import (PYI025)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for from collections.abc import Set imports that do not alias
Set to AbstractSet.
## Why is this bad?
The Set type in collections.abc is an abstract base class for set-like types.
It is easily confused with, and not equivalent to, the set builtin.
To avoid confusion, Set should be aliased to AbstractSet when imported. This
makes it clear that the imported type is an abstract base class, and not the
set builtin.
## Example
```
from collections.abc import Set
```
## Use instead:
```
from collections.abc import Set as AbstractSet
Fix safety
This rule's fix is marked as unsafe for Set imports defined at the
top-level of a .py module. Top-level symbols are implicitly exported by the
module, and so renaming a top-level symbol may break downstream modules
that import it.
The same is not true for .pyi files, where imported symbols are only
re-exported if they are included in __all__, use a "redundant"
import foo as foo alias, or are imported via a * import. As such, the
fix is marked as safe in more cases for .pyi files.
```
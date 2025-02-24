# relative-imports (TID252)
Derived from the flake8-tidy-imports linter.
Fix is sometimes available.
## What it does
Checks for relative imports.
## Why is this bad?
Absolute imports, or relative imports from siblings, are recommended by PEP 8:
Absolute imports are recommended, as they are usually more readable and tend to be better behaved...
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
However, explicit relative imports are an acceptable alternative to absolute imports,
especially when dealing with complex package layouts where using absolute imports would be
unnecessarily verbose:
from . import sibling
from .sibling import example
## Example
```
from .. import foo
```
## Use instead:
```
from mypkg import foo
```
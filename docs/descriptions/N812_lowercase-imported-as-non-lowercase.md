# lowercase-imported-as-non-lowercase (N812)
Derived from the pep8-naming linter.
## What it does
Checks for lowercase imports that are aliased to non-lowercase names.
## Why is this bad?
PEP 8 recommends naming conventions for classes, functions,
constants, and more. The use of inconsistent naming styles between
import and alias names may lead readers to expect an import to be of
another type (e.g., confuse a Python class with a constant).
Import aliases should thus follow the same naming style as the member
being imported.
## Example
```
from example import myclassname as MyClassName
```
## Use instead:
```
from example import myclassname
```
# non-pep585-annotation (UP006)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for the use of generics that can be replaced with standard library
variants based on PEP 585.
## Why is this bad?
PEP 585 enabled collections in the Python standard library (like list)
to be used as generics directly, instead of importing analogous members
from the typing module (like typing.List).
When available, the PEP 585 syntax should be used instead of importing
members from the typing module, as it's more concise and readable.
Importing those members from typing is considered deprecated as of PEP
585.
This rule is enabled when targeting Python 3.9 or later (see:
target-version). By default, it's also enabled for earlier Python
versions if from __future__ import annotations is present, as
__future__ annotations are not evaluated at runtime. If your code relies
on runtime type annotations (either directly or via a library like
Pydantic), you can disable this behavior for Python versions prior to 3.9
by setting lint.pyupgrade.keep-runtime-typing to true.
## Example
```
from typing import List
foo: List[int] = [1, 2, 3]
```
## Use instead:
```
foo: list[int] = [1, 2, 3]
Fix safety
This rule's fix is marked as unsafe, as it may lead to runtime errors when
alongside libraries that rely on runtime type annotations, like Pydantic,
on Python versions prior to Python 3.9.
```
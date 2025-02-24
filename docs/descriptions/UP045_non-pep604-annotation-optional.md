# non-pep604-annotation-optional (UP045)
Derived from the pyupgrade linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Check for typing.Optional annotations that can be rewritten based on PEP 604 syntax.
## Why is this bad?
PEP 604 introduced a new syntax for union type annotations based on the
| operator. This syntax is more concise and readable than the previous
typing.Optional syntax.
This rule is enabled when targeting Python 3.10 or later (see:
target-version). By default, it's also enabled for earlier Python
versions if from __future__ import annotations is present, as
__future__ annotations are not evaluated at runtime. If your code relies
on runtime type annotations (either directly or via a library like
Pydantic), you can disable this behavior for Python versions prior to 3.10
by setting lint.pyupgrade.keep-runtime-typing to true.
## Example
```
from typing import Optional
foo: Optional[int] = None
```
## Use instead:
```
foo: int | None = None
Fix safety
This rule's fix is marked as unsafe, as it may lead to runtime errors when
alongside libraries that rely on runtime type annotations, like Pydantic,
on Python versions prior to Python 3.10. It may also lead to runtime errors
in unusual and likely incorrect type annotations where the type does not
support the | operator.
```
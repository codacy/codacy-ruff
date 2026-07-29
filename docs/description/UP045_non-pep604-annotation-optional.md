# non-pep604-annotation-optional (UP045)
Added in 0.12.0 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is sometimes available.
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
This rule's fix is marked as unsafe on Python versions prior to 3.10 because
using the PEP-604 syntax may lead to runtime errors in libraries that rely
on runtime type annotations, like Pydantic, or in unusual and likely
incorrect type annotations where the type does not support the |
operator. The fix is also marked as unsafe when it would remove comments
present within the type annotation being rewritten.
In preview, this rule can also add its own __future__ import on Python
3.9 and earlier, if the lint.future-annotations setting is enabled. This
also makes the fix unsafe.
```
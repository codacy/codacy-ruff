# implicit-optional (RUF013)
Added in v0.0.273 ·
Related issues ·
View source
Fix is sometimes available.
## What it does
Checks for the use of implicit Optional in type annotations when the
default parameter value is None.
If lint.future-annotations is set to true, from __future__ import annotations will be added if doing so would allow using the | operator on
a Python version before 3.10.
## Why is this bad?
Implicit Optional is prohibited by PEP 484. It is confusing and
inconsistent with the rest of the type system.
It's recommended to use Optional[T] instead. For Python 3.10 and later,
you can also use T | None.
## Example
```
def foo(arg: int = None):
    pass
```
## Use instead:
```
from typing import Optional
def foo(arg: Optional[int] = None):
    pass
Or, for Python 3.10 and later:
def foo(arg: int | None = None):
    pass
If you want to use the | operator in Python 3.9 and earlier, you can
use future imports:
from __future__ import annotations
def foo(arg: int | None = None):
    pass
Limitations
Type aliases and other user-defined types are not supported and could
result in false negatives. For example, the following code will not be
flagged:
Text = str | bytes
class Custom: ...
def foo(text_arg: Text = None, custom_arg: Custom = None):
    pass
```
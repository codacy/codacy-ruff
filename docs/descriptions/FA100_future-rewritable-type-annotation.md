# future-rewritable-type-annotation (FA100)
Derived from the flake8-future-annotations linter.
## What it does
Checks for missing from __future__ import annotations imports upon
detecting type annotations that can be written more succinctly under
PEP 563.
## Why is this bad?
PEP 585 enabled the use of a number of convenient type annotations, such as
list[str] instead of List[str]. However, these annotations are only
available on Python 3.9 and higher, unless the from __future__ import annotations
import is present.
Similarly, PEP 604 enabled the use of the | operator for unions, such as
str | None instead of Optional[str]. However, these annotations are only
available on Python 3.10 and higher, unless the from __future__ import annotations
import is present.
By adding the __future__ import, the pyupgrade rules can automatically
migrate existing code to use the new syntax, even for older Python versions.
This rule thus pairs well with pyupgrade and with Ruff's pyupgrade rules.
This rule respects the target-version setting. For example, if your
project targets Python 3.10 and above, adding from __future__ import annotations
does not impact your ability to leverage PEP 604-style unions (e.g., to
convert Optional[str] to str | None). As such, this rule will only
flag such usages if your project targets Python 3.9 or below.
## Example
```
from typing import List, Dict, Optional
def func(obj: Dict[str, Optional[int]]) -> None: ...
```
## Use instead:
```
from __future__ import annotations
from typing import List, Dict, Optional
def func(obj: Dict[str, Optional[int]]) -> None: ...
After running the additional pyupgrade rules:
from __future__ import annotations
def func(obj: dict[str, int | None]) -> None: ...
```
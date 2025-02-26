# typing-only-first-party-import (TC001)
Derived from the flake8-type-checking linter.
Fix is sometimes available.
## What it does
Checks for first-party imports that are only used for type annotations, but
aren't defined in a type-checking block.
## Why is this bad?
Unused imports add a performance overhead at runtime, and risk creating
import cycles. If an import is only used in typing-only contexts, it can
instead be imported conditionally under an if TYPE_CHECKING: block to
minimize runtime overhead.
If lint.flake8-type-checking.quote-annotations is set to true,
annotations will be wrapped in quotes if doing so would enable the
corresponding import to be moved into an if TYPE_CHECKING: block.
If a class requires that type annotations be available at runtime (as is
the case for Pydantic, SQLAlchemy, and other libraries), consider using
the lint.flake8-type-checking.runtime-evaluated-base-classes and
lint.flake8-type-checking.runtime-evaluated-decorators settings to mark them
as such.
## Example
```
from __future__ import annotations
import local_module
def func(sized: local_module.Container) -> int:
    return len(sized)
```
## Use instead:
```
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import local_module
def func(sized: local_module.Container) -> int:
    return len(sized)
```
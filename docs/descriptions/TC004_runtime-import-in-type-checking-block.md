# runtime-import-in-type-checking-block (TC004)
Derived from the flake8-type-checking linter.
Fix is sometimes available.
## What it does
Checks for imports that are required at runtime but are only defined in
type-checking blocks.
## Why is this bad?
The type-checking block is not executed at runtime, so if the only definition
of a symbol is in a type-checking block, it will not be available at runtime.
If lint.flake8-type-checking.quote-annotations is set to true,
annotations will be wrapped in quotes if doing so would enable the
corresponding import to remain in the type-checking block.
## Example
```
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import foo
def bar() -> None:
    foo.bar()  # raises NameError: name 'foo' is not defined
```
## Use instead:
```
import foo
def bar() -> None:
    foo.bar()
```
# unnecessary-default-type-args (UP043)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary default type arguments for Generator and
AsyncGenerator on Python 3.13+.
## Why is this bad?
Python 3.13 introduced the ability for type parameters to specify default
values. Following this change, several standard-library classes were
updated to add default values for some of their type parameters. For
example, Generator[int] is now equivalent to
Generator[int, None, None], as the second and third type parameters of
Generator now default to None.
Omitting type arguments that match the default values can make the code
more concise and easier to read.
## Example
```
from collections.abc import Generator, AsyncGenerator
def sync_gen() -> Generator[int, None, None]:
    yield 42
async def async_gen() -> AsyncGenerator[int, None]:
    yield 42
```
## Use instead:
```
from collections.abc import Generator, AsyncGenerator
def sync_gen() -> Generator[int]:
    yield 42
async def async_gen() -> AsyncGenerator[int]:
    yield 42
Fix safety
This rule's fix is marked as safe, unless the type annotation contains comments.
```
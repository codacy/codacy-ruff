# multiple-with-statements (SIM117)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for the unnecessary nesting of multiple consecutive context
managers.
## Why is this bad?
In Python 3, a single with block can include multiple context
managers.
Combining multiple context managers into a single with statement
will minimize the indentation depth of the code, making it more
readable.
The following context managers are exempt when used as standalone
statements:
anyio.{CancelScope, fail_after, move_on_after}
asyncio.{timeout, timeout_at}
trio.{fail_after, fail_at, move_on_after, move_on_at}
## Example
```
with A() as a:
    with B() as b:
        pass
```
## Use instead:
```
with A() as a, B() as b:
    pass
```
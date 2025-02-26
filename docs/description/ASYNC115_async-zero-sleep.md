# async-zero-sleep (ASYNC115)
Derived from the flake8-async linter.
Fix is always available.
## What it does
Checks for uses of trio.sleep(0) or anyio.sleep(0).
## Why is this bad?
trio.sleep(0) is equivalent to calling trio.lowlevel.checkpoint().
However, the latter better conveys the intent of the code.
## Example
```
import trio
async def func():
    await trio.sleep(0)
```
## Use instead:
```
import trio
async def func():
    await trio.lowlevel.checkpoint()
```
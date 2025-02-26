# cancel-scope-no-checkpoint (ASYNC100)
Derived from the flake8-async linter.
## What it does
Checks for timeout context managers which do not contain a checkpoint.
For the purposes of this check, yield is considered a checkpoint,
since checkpoints may occur in the caller to which we yield.
## Why is this bad?
Some asynchronous context managers, such as asyncio.timeout and
trio.move_on_after, have no effect unless they contain a checkpoint.
The use of such context managers without an await, async with or
async for statement is likely a mistake.
## Example
```
async def func():
    async with asyncio.timeout(2):
        do_something()
```
## Use instead:
```
async def func():
    async with asyncio.timeout(2):
        do_something()
        await awaitable()
```
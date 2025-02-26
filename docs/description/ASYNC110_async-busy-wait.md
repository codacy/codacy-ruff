# async-busy-wait (ASYNC110)
Derived from the flake8-async linter.
## What it does
Checks for the use of an async sleep function in a while loop.
## Why is this bad?
Instead of sleeping in a while loop, and waiting for a condition
to become true, it's preferable to await on an Event object such
as: asyncio.Event, trio.Event, or anyio.Event.
## Example
```
DONE = False
async def func():
    while not DONE:
        await asyncio.sleep(1)
```
## Use instead:
```
DONE = asyncio.Event()
async def func():
    await DONE.wait()
```
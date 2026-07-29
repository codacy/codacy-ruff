# blocking-input-in-async-function (ASYNC250)
Added in 0.15.0 ·
Related issues ·
View source
Derived from the flake8-async linter.
## What it does
Checks that async functions do not contain blocking usage of input from user.
## Why is this bad?
Blocking an async function via a blocking input call will block the entire
event loop, preventing it from executing other tasks while waiting for user
input, negating the benefits of asynchronous programming.
Instead of making a blocking input call directly, wrap the input call in
an executor to execute the blocking call on another thread.
## Example
```
async def foo():
    username = input("Username:")
```
## Use instead:
```
import asyncio
async def foo():
    loop = asyncio.get_running_loop()
    username = await loop.run_in_executor(None, input, "Username:")
```
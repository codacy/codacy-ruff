# blocking-path-method-in-async-function (ASYNC240)
Added in 0.15.0 ·
Related issues ·
View source
Derived from the flake8-async linter.
## What it does
Checks that async functions do not call blocking os.path functions or
pathlib.Path methods.
## Why is this bad?
Calling some os.path functions or pathlib.Path methods in an async function
will block the entire event loop, preventing it from executing other tasks while
waiting for the operation. This negates the benefits of asynchronous programming.
Instead, run blocking path operations in a separate thread, or use an API that
provides asynchronous path operations, such as aiofiles.os.path, anyio.Path,
or trio.Path.
## Example
```
import os
async def func():
    path = "my_file.txt"
    file_exists = os.path.exists(path)
On Python 3.9 and later, use instead:
import asyncio
import os
async def func():
    path = "my_file.txt"
    file_exists = await asyncio.to_thread(os.path.exists, path)
On earlier Python versions, use loop.run_in_executor().
Or, use an asynchronous path API:
import trio
async def func():
    path = trio.Path("my_file.txt")
    file_exists = await path.exists()
Purely computational path operations, such as os.path.join() and
pathlib.Path.with_suffix(), are not flagged.
```
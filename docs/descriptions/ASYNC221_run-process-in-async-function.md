# run-process-in-async-function (ASYNC221)
Derived from the flake8-async linter.
## What it does
Checks that async functions do not run processes with blocking methods.
## Why is this bad?
Blocking an async function via a blocking call will block the entire
event loop, preventing it from executing other tasks while waiting for the
call to complete, negating the benefits of asynchronous programming.
Instead of making a blocking call, use an equivalent asynchronous library
or function, like trio.run_process()
or anyio.run_process().
## Example
```
async def foo():
    subprocess.run(cmd)
```
## Use instead:
```
async def foo():
    asyncio.create_subprocess_shell(cmd)
```
# asyncio-dangling-task (RUF006)
## What it does
Checks for asyncio.create_task and asyncio.ensure_future calls
that do not store a reference to the returned result.
## Why is this bad?
Per the asyncio documentation, the event loop only retains a weak
reference to tasks. If the task returned by asyncio.create_task and
asyncio.ensure_future is not stored in a variable, or a collection,
or otherwise referenced, it may be garbage collected at any time. This
can lead to unexpected and inconsistent behavior, as your tasks may or
may not run to completion.
## Example
```
import asyncio
for i in range(10):
    # This creates a weak reference to the task, which may be garbage
    # collected at any time.
    asyncio.create_task(some_coro(param=i))
```
## Use instead:
```
import asyncio
background_tasks = set()
for i in range(10):
    task = asyncio.create_task(some_coro(param=i))
    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)
    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)
```
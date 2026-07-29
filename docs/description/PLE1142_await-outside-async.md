# await-outside-async (PLE1142)
Added in v0.0.150 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for uses of await outside async functions.
## Why is this bad?
Using await outside an async function is a syntax error.
## Example
```
import asyncio
def foo():
    await asyncio.sleep(1)
```
## Use instead:
```
import asyncio
async def foo():
    await asyncio.sleep(1)
Notebook behavior
As an exception, await is allowed at the top level of a Jupyter notebook
(see: autoawait).
```
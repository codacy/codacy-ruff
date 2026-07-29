# blocking-http-call-httpx-in-async-function (ASYNC212)
Added in 0.15.0 ·
Related issues ·
View source
Derived from the flake8-async linter.
## What it does
Checks that async functions do not use blocking httpx clients.
## Why is this bad?
Blocking an async function via a blocking HTTP call will block the entire
event loop, preventing it from executing other tasks while waiting for the
HTTP response, negating the benefits of asynchronous programming.
Instead of using the blocking httpx client, use the asynchronous client.
## Example
```
import httpx
async def fetch():
    client = httpx.Client()
    response = client.get(...)
```
## Use instead:
```
import httpx
async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get(...)
```
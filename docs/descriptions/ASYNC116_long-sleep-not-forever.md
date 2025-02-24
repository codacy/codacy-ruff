# long-sleep-not-forever (ASYNC116)
Derived from the flake8-async linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of trio.sleep() or anyio.sleep() with a delay greater than 24 hours.
## Why is this bad?
Calling sleep() with a delay greater than 24 hours is usually intended
to sleep indefinitely. Instead of using a large delay,
trio.sleep_forever() or anyio.sleep_forever() better conveys the intent.
## Example
```
import trio
async def func():
    await trio.sleep(86401)
```
## Use instead:
```
import trio
async def func():
    await trio.sleep_forever()
```
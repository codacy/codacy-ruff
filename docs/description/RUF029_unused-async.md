# unused-async (RUF029)
Preview (since v0.4.0) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for functions declared async that do not await or otherwise use features requiring the
function to be declared async.
## Why is this bad?
Declaring a function async when it's not is usually a mistake, and will artificially limit the
contexts where that function may be called. In some cases, labeling a function async is
semantically meaningful. For example, an async test or callback may need to run in an async
execution context, even if it only uses a ContextVar.
If the async context is intentional, add an actual await expression, such as
await asyncio.sleep(0), or disable this rule for the function.
## Example
```
async def foo():
    bar()
```
## Use instead:
```
def foo():
    bar()
```
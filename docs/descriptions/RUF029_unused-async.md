# unused-async (RUF029)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for functions declared async that do not await or otherwise use features requiring the
function to be declared async.
## Why is this bad?
Declaring a function async when it's not is usually a mistake, and will artificially limit the
contexts where that function may be called. In some cases, labeling a function async is
semantically meaningful (e.g. with the trio library).
## Examples
```
async def foo():
    bar()
```
## Use instead:
```
def foo():
    bar()
```
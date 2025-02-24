# yield-from-in-async-function (PLE1700)
Derived from the Pylint linter.
## What it does
Checks for uses of yield from in async functions.
## Why is this bad?
Python doesn't support the use of yield from in async functions, and will
raise a SyntaxError in such cases.
Instead, considering refactoring the code to use an async for loop instead.
## Example
```
async def numbers():
    yield from [1, 2, 3, 4, 5]
```
## Use instead:
```
async def numbers():
    async for number in [1, 2, 3, 4, 5]:
        yield number
```
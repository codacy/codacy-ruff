# async-function-with-timeout (ASYNC109)
Added in 0.5.0 ·
Related issues ·
View source
Derived from the flake8-async linter.
## What it does
Checks for async function definitions with timeout parameters.
## Why is this bad?
Rather than implementing asynchronous timeout behavior manually, prefer
built-in timeout functionality, such as asyncio.timeout, trio.fail_after,
or anyio.move_on_after, among others.
This rule is highly opinionated to enforce a design pattern
called "structured concurrency" that allows for
async functions to be oblivious to timeouts,
instead letting callers to handle the logic with a context manager.
Details
This rule attempts to detect which async framework your code is using
by analysing the imports in the file it's checking. If it sees an
anyio import in your code, it will assume anyio is your framework
of choice; if it sees a trio import, it will assume trio; if it
sees neither, it will assume asyncio. asyncio.timeout was added
in Python 3.11, so if asyncio is detected as the framework being used,
this rule will be ignored when your configured target-version is set
to less than Python 3.11.
For functions that wrap asyncio.timeout, trio.fail_after or
anyio.move_on_after, false positives from this rule can be avoided
by using a different parameter name.
This rule exempts methods decorated with @typing.override.
Removing a parameter from a subclass method may cause type checkers to
complain about a violation of the Liskov Substitution Principle if it
means that the method now incompatibly overrides a method defined on a
superclass. Explicitly decorating an overriding method with @override
signals to Ruff that the method is intended to override a superclass
method and that a type checker will enforce that it does so; Ruff
therefore knows that it should not enforce this rule on such methods.
## Example
```
async def long_running_task(timeout): ...
async def main():
    await long_running_task(timeout=2)
```
## Use instead:
```
async def long_running_task(): ...
async def main():
    async with asyncio.timeout(2):
        await long_running_task()
```
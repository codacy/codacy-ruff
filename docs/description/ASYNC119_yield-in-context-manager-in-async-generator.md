# yield-in-context-manager-in-async-generator (ASYNC119)
Preview (since 0.15.16) ·
Related issues ·
View source
Derived from the flake8-async linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for yield inside a context manager in an async generator.
## Why is this bad?
Yielding inside a context manager in an async generator is unsafe because
the cleanup of the context manager may be delayed until the generator is
closed, at which point await is no longer allowed. This can lead to
resource leaks or other bugs.
For more information, see PEP 533.
If the function is intended to yield only once and act as a context
manager, use @asynccontextmanager. If it's a true async generator
that yields multiple values, consumers should use contextlib.aclosing to
ensure timely cleanup, or the generator should be refactored to avoid
holding context managers open across yields.
The rule also suppresses diagnostics for functions decorated with
@pytest.fixture, @pytest_asyncio.fixture, or @trio.as_safe_channel,
as these handle async generator cleanup safely.
## Example
```
The following function yields once inside a context manager, but without
@asynccontextmanager, cleanup of the connection may be delayed:
async def open_connection():
    async with connect() as conn:
        yield conn
If the function is intended to yield exactly once (i.e., it's a context
manager), add @asynccontextmanager:
from contextlib import asynccontextmanager
@asynccontextmanager
async def open_connection():
    async with connect() as conn:
        yield conn
For async generators that yield multiple values, @asynccontextmanager
is not appropriate. Instead, refactor to avoid holding context managers
open across yields, or ensure consumers use contextlib.aclosing for timely
cleanup.
Known problems
Using contextlib.aclosing around all call sites of an async generator is a
valid way to guarantee timely cleanup, but this rule cannot verify that
all callers use aclosing. As a result, it may flag generators that
are always consumed safely.
```
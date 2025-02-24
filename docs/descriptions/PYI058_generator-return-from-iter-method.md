# generator-return-from-iter-method (PYI058)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for simple __iter__ methods that return Generator, and for
simple __aiter__ methods that return AsyncGenerator.
## Why is this bad?
Using (Async)Iterator for these methods is simpler and more elegant. More
importantly, it also reflects the fact that the precise kind of iterator
returned from an __iter__ method is usually an implementation detail that
could change at any time. Type annotations help define a contract for a
function; implementation details should not leak into that contract.
For example:
from collections.abc import AsyncGenerator, Generator
from typing import Any
class CustomIterator:
    def __iter__(self) -> Generator:
        yield from range(42)
class CustomIterator2:
    def __iter__(self) -> Generator[str, Any, None]:
        yield from "abcdefg"
```
## Use instead:
```
from collections.abc import Iterator
class CustomIterator:
    def __iter__(self) -> Iterator:
        yield from range(42)
class CustomIterator2:
    def __iter__(self) -> Iterator[str]:
        yield from "abdefg"
Fix safety
This rule tries hard to avoid false-positive errors, and the rule's fix
should always be safe for .pyi stub files. However, there is a slightly
higher chance that a false positive might be emitted by this rule when
applied to runtime Python (.py files). As such, the fix is marked as
unsafe for any __iter__ or __aiter__ method in a .py file that has
more than two statements (including docstrings) in its body.
```
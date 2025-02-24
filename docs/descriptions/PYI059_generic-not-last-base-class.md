# generic-not-last-base-class (PYI059)
Derived from the flake8-pyi linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for classes inheriting from typing.Generic[] where Generic[] is
not the last base class in the bases tuple.
## Why is this bad?
If Generic[] is not the final class in the bases tuple, unexpected
behaviour can occur at runtime (See this CPython issue for an example).
The rule is also applied to stub files, but, unlike at runtime,
in stubs it is purely enforced for stylistic consistency.
For example:
class LinkedList(Generic[T], Sized):
    def push(self, item: T) -> None:
        self._items.append(item)
class MyMapping(
    Generic[K, V],
    Iterable[Tuple[K, V]],
    Container[Tuple[K, V]],
):
    ...
```
## Use instead:
```
class LinkedList(Sized, Generic[T]):
    def push(self, item: T) -> None:
        self._items.append(item)
class MyMapping(
    Iterable[Tuple[K, V]],
    Container[Tuple[K, V]],
    Generic[K, V],
):
    ...
```
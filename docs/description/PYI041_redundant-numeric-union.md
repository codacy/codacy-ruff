# redundant-numeric-union (PYI041)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for parameter annotations that contain redundant unions between
builtin numeric types (e.g., int | float).
## Why is this bad?
The typing specification states:
Python’s numeric types complex, float and int are not subtypes of
each other, but to support common use cases, the type system contains a
straightforward shortcut: when an argument is annotated as having type
float, an argument of type int is acceptable; similar, for an
argument annotated as having type complex, arguments of type float or
int are acceptable.
As such, a union that includes both int and float is redundant in the
specific context of a parameter annotation, as it is equivalent to a union
that only includes float. For readability and clarity, unions should omit
redundant elements.
## Example
```
def foo(x: float | int | str) -> None: ...
```
## Use instead:
```
def foo(x: float | str) -> None: ...
Fix safety
This rule's fix is marked as safe, unless the type annotation contains comments.
Note that while the fix may flatten nested unions into a single top-level union,
the semantics of the annotation will remain unchanged.
```
# quoted-annotation (UP037)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for the presence of unnecessary quotes in type annotations.
## Why is this bad?
In Python, type annotations can be quoted to avoid forward references.
However, if from __future__ import annotations is present, Python
will always evaluate type annotations in a deferred manner, making
the quotes unnecessary.
Similarly, if the annotation is located in a typing-only context and
won't be evaluated by Python at runtime, the quotes will also be
considered unnecessary. For example, Python does not evaluate type
annotations on assignments in function bodies.
## Example
```
Given:
from __future__ import annotations
def foo(bar: "Bar") -> "Bar": ...
```
## Use instead:
```
from __future__ import annotations
def foo(bar: Bar) -> Bar: ...
Given:
def foo() -> None:
    bar: "Bar"
```
## Use instead:
```
def foo() -> None:
    bar: Bar
See also
quoted-annotation-in-stub: A rule that
    removes all quoted annotations from stub files
quoted-type-alias: A rule that removes unnecessary quotes
    from type aliases.
```
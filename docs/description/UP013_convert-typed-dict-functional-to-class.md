# convert-typed-dict-functional-to-class (UP013)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for TypedDict declarations that use functional syntax.
## Why is this bad?
TypedDict types can be defined either through a functional syntax
(Foo = TypedDict(...)) or a class syntax (class Foo(TypedDict): ...).
The class syntax is more readable and generally preferred over the
functional syntax.
Nonetheless, there are some situations in which it is impossible to use
the class-based syntax. This rule will not apply to those cases. Namely,
it is impossible to use the class-based syntax if any TypedDict fields are:
Not valid python identifiers (for example, @x)
Python keywords such as in
Private names such as __id that would undergo name mangling at runtime
    if the class-based syntax was used
Dunder names such as __int__ that can confuse type checkers if they're used
    with the class-based syntax.
## Example
```
from typing import TypedDict
Foo = TypedDict("Foo", {"a": int, "b": str})
```
## Use instead:
```
from typing import TypedDict
class Foo(TypedDict):
    a: int
    b: str
Fix safety
This rule's fix is marked as unsafe if there are any comments within the
range of the TypedDict definition, as these will be dropped by the
autofix.
```
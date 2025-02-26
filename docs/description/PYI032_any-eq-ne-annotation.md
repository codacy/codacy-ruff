# any-eq-ne-annotation (PYI032)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for __eq__ and __ne__ implementations that use typing.Any as
the type annotation for their second parameter.
## Why is this bad?
The Python documentation recommends the use of object to "indicate that a
value could be any type in a typesafe manner". Any, on the other hand,
should be seen as an "escape hatch when you need to mix dynamically and
statically typed code". Since using Any allows you to write highly unsafe
code, you should generally only use Any when the semantics of your code
would otherwise be inexpressible to the type checker.
The expectation in Python is that a comparison of two arbitrary objects
using == or != should never raise an exception. This contract can be
fully expressed in the type system and does not involve requesting unsound
behaviour from a type checker. As such, object is a more appropriate
annotation than Any for the second parameter of the methods implementing
these comparison operators -- __eq__ and __ne__.
## Example
```
class Foo:
    def __eq__(self, obj: typing.Any) -> bool: ...
```
## Use instead:
```
class Foo:
    def __eq__(self, obj: object) -> bool: ...
```
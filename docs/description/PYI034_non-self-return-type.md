# non-self-return-type (PYI034)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for methods that are annotated with a fixed return type which
should instead be returning Self.
## Why is this bad?
If methods that generally return self at runtime are annotated with a
fixed return type, and the class is subclassed, type checkers will not be
able to infer the correct return type.
For example:
class Shape:
    def set_scale(self, scale: float) -> Shape:
        self.scale = scale
        return self
class Circle(Shape):
    def set_radius(self, radius: float) -> Circle:
        self.radius = radius
        return self
# Type checker infers return type as `Shape`, not `Circle`.
Circle().set_scale(0.5)
# Thus, this expression is invalid, as `Shape` has no attribute `set_radius`.
Circle().set_scale(0.5).set_radius(2.7)
Specifically, this check enforces that the return type of the following
methods is Self:
In-place binary-operation dunder methods, like __iadd__, __imul__, etc.
__new__, __enter__, and __aenter__, if those methods return the
    class name.
__iter__ methods that return Iterator, despite the class inheriting
    directly from Iterator.
__aiter__ methods that return AsyncIterator, despite the class
    inheriting directly from AsyncIterator.
## Example
```
class Foo:
    def __new__(cls, *args: Any, **kwargs: Any) -> Foo: ...
    def __enter__(self) -> Foo: ...
    async def __aenter__(self) -> Foo: ...
    def __iadd__(self, other: Foo) -> Foo: ...
```
## Use instead:
```
from typing_extensions import Self
class Foo:
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    def __enter__(self) -> Self: ...
    async def __aenter__(self) -> Self: ...
    def __iadd__(self, other: Foo) -> Self: ...
Fix safety
This rule's fix is marked as unsafe as it changes the meaning of your type annotations.
```
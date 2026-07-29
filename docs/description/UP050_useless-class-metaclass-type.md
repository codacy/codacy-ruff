# useless-class-metaclass-type (UP050)
Added in 0.13.0 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for metaclass=type in class definitions.
## Why is this bad?
Since Python 3, the default metaclass is type, so specifying it explicitly is redundant.
Even though __prepare__ is not required, the default metaclass (type) implements it,
for the convenience of subclasses calling it via super().
## Example
```
class Foo(metaclass=type): ...
```
## Use instead:
```
class Foo: ...
```
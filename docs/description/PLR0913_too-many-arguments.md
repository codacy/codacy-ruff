# too-many-arguments (PLR0913)
Added in v0.0.238 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for function definitions that include too many arguments.
By default, this rule allows up to five arguments, as configured by the
lint.pylint.max-args option.
This rule exempts methods decorated with @typing.override.
Changing the signature of a subclass method may cause type checkers to
complain about a violation of the Liskov Substitution Principle if it
means that the method now incompatibly overrides a method defined on a
superclass. Explicitly decorating an overriding method with @override
signals to Ruff that the method is intended to override a superclass
method and that a type checker will enforce that it does so; Ruff
therefore knows that it should not enforce rules about methods having
too many arguments.
## Why is this bad?
Functions with many arguments are harder to understand, maintain, and call.
Consider refactoring functions with many arguments into smaller functions
with fewer arguments, or using objects to group related arguments.
## Example
```
def calculate_position(x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, time):
    new_x = x_pos + x_vel * time
    new_y = y_pos + y_vel * time
    new_z = z_pos + z_vel * time
    return new_x, new_y, new_z
```
## Use instead:
```
from typing import NamedTuple
class Vector(NamedTuple):
    x: float
    y: float
    z: float
def calculate_position(pos: Vector, vel: Vector, time: float) -> Vector:
    return Vector(*(p + v * time for p, v in zip(pos, vel)))
```
# too-many-positional-arguments (PLR0917)
Added in 0.16.0 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for function definitions that include too many positional arguments.
By default, this rule allows up to five arguments, as configured by the
lint.pylint.max-positional-args option.
## Why is this bad?
Functions with many arguments are harder to understand, maintain, and call.
This is especially true for functions with many positional arguments, as
providing arguments positionally is more error-prone and less clear to
readers than providing arguments by name.
Consider refactoring functions with many arguments into smaller functions
with fewer arguments, using objects to group related arguments, or migrating to
keyword-only arguments.
This rule exempts methods decorated with @typing.override.
Changing the signature of a subclass method may cause type checkers to
complain about a violation of the Liskov Substitution Principle if it
means that the method now incompatibly overrides a method defined on a
superclass. Explicitly decorating an overriding method with @override
signals to Ruff that the method is intended to override a superclass
method and that a type checker will enforce that it does so; Ruff
therefore knows that it should not enforce rules about methods having
too many arguments.
## Example
```
def plot(x, y, z, color, mark, add_trendline): ...
plot(1, 2, 3, "r", "*", True)
```
## Use instead:
```
def plot(x, y, z, *, color, mark, add_trendline): ...
plot(1, 2, 3, color="r", mark="*", add_trendline=True)
```
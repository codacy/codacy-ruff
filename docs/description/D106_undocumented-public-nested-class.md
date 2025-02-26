# undocumented-public-nested-class (D106)
Derived from the pydocstyle linter.
## What it does
Checks for undocumented public class definitions, for nested classes.
## Why is this bad?
Public classes should be documented via docstrings to outline their
purpose and behavior.
Nested classes do not inherit the docstring of their enclosing class, so
they should have their own docstrings.
If the codebase adheres to a standard format for class docstrings, follow
that format for consistency.
## Example
```
class Foo:
    """Class Foo."""
    class Bar: ...
bar = Foo.Bar()
bar.__doc__  # None
```
## Use instead:
```
class Foo:
    """Class Foo."""
    class Bar:
        """Class Bar."""
bar = Foo.Bar()
bar.__doc__  # "Class Bar."
```
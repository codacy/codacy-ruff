# undocumented-public-init (D107)
Derived from the pydocstyle linter.
## What it does
Checks for public __init__ method definitions that are missing
docstrings.
## Why is this bad?
Public __init__ methods are used to initialize objects. __init__
methods should be documented via docstrings to describe the method's
behavior, arguments, side effects, exceptions, and any other information
that may be relevant to the user.
If the codebase adheres to a standard format for __init__ method docstrings,
follow that format for consistency.
## Example
```
class City:
    def __init__(self, name: str, population: int) -> None:
        self.name: str = name
        self.population: int = population
```
## Use instead:
```
class City:
    def __init__(self, name: str, population: int) -> None:
        """Initialize a city with a name and population."""
        self.name: str = name
        self.population: int = population
```
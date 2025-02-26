# undocumented-magic-method (D105)
Derived from the pydocstyle linter.
## What it does
Checks for undocumented magic method definitions.
## Why is this bad?
Magic methods (methods with names that start and end with double
underscores) are used to implement operator overloading and other special
behavior. Such methods should be documented via docstrings to
outline their behavior.
Generally, magic method docstrings should describe the method's behavior,
arguments, side effects, exceptions, return values, and any other
information that may be relevant to the user.
If the codebase adheres to a standard format for method docstrings, follow
that format for consistency.
## Example
```
class Cat(Animal):
    def __str__(self) -> str:
        return f"Cat: {self.name}"
cat = Cat("Dusty")
print(cat)  # "Cat: Dusty"
```
## Use instead:
```
class Cat(Animal):
    def __str__(self) -> str:
        """Return a string representation of the cat."""
        return f"Cat: {self.name}"
cat = Cat("Dusty")
print(cat)  # "Cat: Dusty"
```
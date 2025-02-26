# undocumented-public-method (D102)
Derived from the pydocstyle linter.
## What it does
Checks for undocumented public method definitions.
## Why is this bad?
Public methods should be documented via docstrings to outline their purpose
and behavior.
Generally, a method docstring should describe the method's behavior,
arguments, side effects, exceptions, return values, and any other
information that may be relevant to the user.
If the codebase adheres to a standard format for method docstrings, follow
that format for consistency.
## Example
```
class Cat(Animal):
    def greet(self, happy: bool = True):
        if happy:
            print("Meow!")
        else:
            raise ValueError("Tried to greet an unhappy cat.")
Use instead (in the NumPy docstring format):
class Cat(Animal):
    def greet(self, happy: bool = True):
        """Print a greeting from the cat.
        Parameters
        ----------
        happy : bool, optional
            Whether the cat is happy, is True by default.
        Raises
        ------
        ValueError
            If the cat is not happy.
        """
        if happy:
            print("Meow!")
        else:
            raise ValueError("Tried to greet an unhappy cat.")
Or (in the Google docstring format):
class Cat(Animal):
    def greet(self, happy: bool = True):
        """Print a greeting from the cat.
        Args:
            happy: Whether the cat is happy, is True by default.
        Raises:
            ValueError: If the cat is not happy.
        """
        if happy:
            print("Meow!")
        else:
            raise ValueError("Tried to greet an unhappy cat.")
```
# property-with-parameters (PLR0206)
Derived from the Pylint linter.
## What it does
Checks for property definitions that accept function parameters.
## Why is this bad?
Properties cannot be called with parameters.
If you need to pass parameters to a property, create a method with the
desired parameters and call that method instead.
## Example
```
class Cat:
    @property
    def purr(self, volume): ...
```
## Use instead:
```
class Cat:
    @property
    def purr(self): ...
    def purr_volume(self, volume): ...
```
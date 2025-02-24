# too-many-public-methods (PLR0904)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for classes with too many public methods
By default, this rule allows up to 20 public methods, as configured by
the lint.pylint.max-public-methods option.
## Why is this bad?
Classes with many public methods are harder to understand
and maintain.
Instead, consider refactoring the class into separate classes.
## Example
```
Assuming that lint.pylint.max-public-methods is set to 5:
class Linter:
    def __init__(self):
        pass
    def pylint(self):
        pass
    def pylint_settings(self):
        pass
    def flake8(self):
        pass
    def flake8_settings(self):
        pass
    def pydocstyle(self):
        pass
    def pydocstyle_settings(self):
        pass
```
## Use instead:
```
class Linter:
    def __init__(self):
        self.pylint = Pylint()
        self.flake8 = Flake8()
        self.pydocstyle = Pydocstyle()
    def lint(self):
        pass
class Pylint:
    def lint(self):
        pass
    def settings(self):
        pass
class Flake8:
    def lint(self):
        pass
    def settings(self):
        pass
class Pydocstyle:
    def lint(self):
        pass
    def settings(self):
        pass
```
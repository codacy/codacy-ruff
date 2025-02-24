# invalid-first-argument-name-for-class-method (N804)
Derived from the pep8-naming linter.
Fix is sometimes available.
## What it does
Checks for class methods that use a name other than cls for their
first argument.
With preview enabled, the method __new__ is exempted from this
check and the corresponding violation is then caught by
bad-staticmethod-argument.
## Why is this bad?
PEP 8 recommends the use of cls as the first argument for all class
methods:
Always use cls for the first argument to class methods.
If a function argument’s name clashes with a reserved keyword, it is generally better to
append a single trailing underscore rather than use an abbreviation or spelling corruption.
Thus class_ is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)
Names can be excluded from this rule using the lint.pep8-naming.ignore-names
or lint.pep8-naming.extend-ignore-names configuration options. For example,
to allow the use of klass as the first argument to class methods, set
the lint.pep8-naming.extend-ignore-names option to ["klass"].
## Example
```
class Example:
    @classmethod
    def function(self, data): ...
```
## Use instead:
```
class Example:
    @classmethod
    def function(cls, data): ...
Fix safety
This rule's fix is marked as unsafe, as renaming a method parameter
can change the behavior of the program.
```
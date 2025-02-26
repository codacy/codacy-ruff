# invalid-first-argument-name-for-method (N805)
Derived from the pep8-naming linter.
Fix is sometimes available.
## What it does
Checks for instance methods that use a name other than self for their
first argument.
## Why is this bad?
PEP 8 recommends the use of self as first argument for all instance
methods:
Always use self for the first argument to instance methods.
If a function argument’s name clashes with a reserved keyword, it is generally better to
append a single trailing underscore rather than use an abbreviation or spelling corruption.
Thus class_ is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)
Names can be excluded from this rule using the lint.pep8-naming.ignore-names
or lint.pep8-naming.extend-ignore-names configuration options. For example,
to allow the use of this as the first argument to instance methods, set
the lint.pep8-naming.extend-ignore-names option to ["this"].
## Example
```
class Example:
    def function(cls, data): ...
```
## Use instead:
```
class Example:
    def function(self, data): ...
Fix safety
This rule's fix is marked as unsafe, as renaming a method parameter
can change the behavior of the program.
```
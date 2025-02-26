# bad-staticmethod-argument (PLW0211)
Derived from the Pylint linter.
## What it does
Checks for static methods that use self or cls as their first argument.
If preview mode is enabled, this rule also applies to
__new__ methods, which are implicitly static.
## Why is this bad?
PEP 8 recommends the use of self and cls as the first arguments for
instance methods and class methods, respectively. Naming the first argument
of a static method as self or cls can be misleading, as static methods
do not receive an instance or class reference as their first argument.
## Example
```
class Wolf:
    @staticmethod
    def eat(self):
        pass
```
## Use instead:
```
class Wolf:
    @staticmethod
    def eat(sheep):
        pass
```
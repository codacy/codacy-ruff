# invalid-class-name (N801)
Derived from the pep8-naming linter.
## What it does
Checks for class names that do not follow the CamelCase convention.
## Why is this bad?
PEP 8 recommends the use of the CapWords (or CamelCase) convention
for class names:
Class names should normally use the CapWords convention.
The naming convention for functions may be used instead in cases where the interface is
documented and used primarily as a callable.
Note that there is a separate convention for builtin names: most builtin names are single
words (or two words run together), with the CapWords convention used only for exception
names and builtin constants.
## Example
```
class my_class:
    pass
```
## Use instead:
```
class MyClass:
    pass
```
# unused-static-method-argument (ARG004)
Added in v0.0.168 ·
Related issues ·
View source
Derived from the flake8-unused-arguments linter.
## What it does
Checks for the presence of unused arguments in static method definitions.
## Why is this bad?
An argument that is defined but not used is likely a mistake, and should
be removed to avoid confusion.
If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
lint.dummy-variable-rgx pattern.
This rule exempts methods decorated with @typing.override.
Removing a parameter from a subclass method (or changing a parameter's
name) may cause type checkers to complain about a violation of the Liskov
Substitution Principle if it means that the method now incompatibly
overrides a method defined on a superclass. Explicitly decorating an
overriding method with @override signals to Ruff that the method is
intended to override a superclass method, and that a type checker will
enforce that it does so; Ruff therefore knows that it should not enforce
rules about unused arguments on such methods.
## Example
```
class Class:
    @staticmethod
    def foo(arg1, arg2):
        print(arg1)
```
## Use instead:
```
class Class:
    @staticmethod
    def foo(arg1):
        print(arg1)
```
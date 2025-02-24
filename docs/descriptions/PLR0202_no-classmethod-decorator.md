# no-classmethod-decorator (PLR0202)
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for the use of a classmethod being made without the decorator.
## Why is this bad?
When it comes to consistency and readability, it's preferred to use the decorator.
## Example
```
class Foo:
    def bar(cls): ...
    bar = classmethod(bar)
```
## Use instead:
```
class Foo:
    @classmethod
    def bar(cls): ...
```
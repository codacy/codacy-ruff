# typed-argument-default-in-stub (PYI011)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for typed function arguments in stubs with complex default values.
## Why is this bad?
Stub (.pyi) files exist as "data files" for static analysis tools, and
are not evaluated at runtime. While simple default values may be useful for
some tools that consume stubs, such as IDEs, they are ignored by type
checkers.
Instead of including and reproducing a complex value, use ... to indicate
that the assignment has a default value, but that the value is "complex" or
varies according to the current platform or Python version. For the
purposes of this rule, any default value counts as "complex" unless it is
a literal int, float, complex, bytes, str, bool, None, ...,
or a simple container literal.
## Example
```
def foo(arg: list[int] = list(range(10_000))) -> None: ...
```
## Use instead:
```
def foo(arg: list[int] = ...) -> None: ...
```
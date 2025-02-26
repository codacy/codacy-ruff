# numeric-literal-too-long (PYI054)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for numeric literals with a string representation longer than ten
characters.
## Why is this bad?
If a function has a default value where the literal representation is
greater than 50 characters, the value is likely to be an implementation
detail or a constant that varies depending on the system you're running on.
Default values like these should generally be omitted from stubs. Use
ellipses (...) instead.
## Example
```
def foo(arg: int = 693568516352839939918568862861217771399698285293568) -> None: ...
```
## Use instead:
```
def foo(arg: int = ...) -> None: ...
```
# string-or-bytes-too-long (PYI053)
Added in v0.0.271 ·
Related issues ·
View source
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for the use of string and bytes literals longer than 50 characters
in stub (.pyi) files.
## Why is this bad?
If a function or variable has a default value where the string or bytes
representation is greater than 50 characters long, it is likely to be an
implementation detail or a constant that varies depending on the system
you're running on.
Although IDEs may find them useful, default values are ignored by type
checkers, the primary consumers of stub files. Replace very long constants
with ellipses (...) to simplify the stub.
The rule does not apply to long entries in __all__, which are assumed to
be outside the stub author's control.
## Example
```
def foo(arg: str = "51 character stringgggggggggggggggggggggggggggggggg") -> None: ...
```
## Use instead:
```
def foo(arg: str = ...) -> None: ...
```
# pep484-style-positional-only-parameter (PYI063)
Derived from the flake8-pyi linter.
## What it does
Checks for the presence of PEP 484-style positional-only parameters.
## Why is this bad?
Historically, PEP 484 recommended prefixing parameter names with double
underscores (__) to indicate to a type checker that they were
positional-only. However, PEP 570 (introduced in Python 3.8) introduced
dedicated syntax for positional-only arguments. If a forward slash (/) is
present in a function signature on Python 3.8+, all parameters prior to the
slash are interpreted as positional-only.
The new syntax should be preferred as it is more widely used, more concise
and more readable. It is also respected by Python at runtime, whereas the
old-style syntax was only understood by type checkers.
## Example
```
def foo(__x: int) -> None: ...
```
## Use instead:
```
def foo(x: int, /) -> None: ...
```
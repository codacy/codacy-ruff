# debugger (T100)
Derived from the flake8-debugger linter.
## What it does
Checks for the presence of debugger calls and imports.
## Why is this bad?
Debugger calls and imports should be used for debugging purposes only. The
presence of a debugger call or import in production code is likely a
mistake and may cause unintended behavior, such as exposing sensitive
information or causing the program to hang.
Instead, consider using a logging library to log information about the
program's state, and writing tests to verify that the program behaves
as expected.
## Example
```
def foo():
    breakpoint()
```
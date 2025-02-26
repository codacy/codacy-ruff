# os-error-alias (UP024)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of exceptions that alias OSError.
## Why is this bad?
OSError is the builtin error type used for exceptions that relate to the
operating system.
In Python 3.3, a variety of other exceptions, like WindowsError were
aliased to OSError. These aliases remain in place for compatibility with
older versions of Python, but may be removed in future versions.
Prefer using OSError directly, as it is more idiomatic and future-proof.
## Example
```
raise IOError
```
## Use instead:
```
raise OSError
```
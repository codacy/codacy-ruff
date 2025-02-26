# continue-in-finally (PLE0116)
Derived from the Pylint linter.
## What it does
Checks for continue statements inside finally
## Why is this bad?
continue statements were not allowed within finally clauses prior to
Python 3.8. Using a continue statement within a finally clause can
cause a SyntaxError.
## Example
```
while True:
    try:
        pass
    finally:
        continue
```
## Use instead:
```
while True:
    try:
        pass
    except Exception:
        pass
    else:
        continue
```
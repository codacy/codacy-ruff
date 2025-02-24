# sys-exit-alias (PLR1722)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for uses of the exit() and quit().
## Why is this bad?
exit and quit come from the site module, which is typically imported
automatically during startup. However, it is not guaranteed to be
imported, and so using these functions may result in a NameError at
runtime. Generally, these constants are intended to be used in an interactive
interpreter, and not in programs.
Prefer sys.exit(), as the sys module is guaranteed to exist in all
contexts.
## Example
```
if __name__ == "__main__":
    exit()
```
## Use instead:
```
import sys
if __name__ == "__main__":
    sys.exit()
```
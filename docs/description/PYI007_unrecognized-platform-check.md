# unrecognized-platform-check (PYI007)
Derived from the flake8-pyi linter.
## What it does
Check for unrecognized sys.platform checks. Platform checks should be
simple string comparisons.
Note: this rule is only enabled in .pyi stub files.
## Why is this bad?
Some sys.platform checks are too complex for type checkers to
understand, and thus result in incorrect inferences by these tools.
sys.platform checks should be simple string comparisons, like
if sys.platform == "linux".
## Example
```
if sys.platform.startswith("linux"):
    # Linux specific definitions
    ...
else:
    # Posix specific definitions
    ...
Instead, use a simple string comparison, such as == or !=:
if sys.platform == "linux":
    # Linux specific definitions
    ...
else:
    # Posix specific definitions
    ...
```
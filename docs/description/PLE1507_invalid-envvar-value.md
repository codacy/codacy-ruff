# invalid-envvar-value (PLE1507)
Derived from the Pylint linter.
## What it does
Checks for os.getenv calls with an invalid key argument.
## Why is this bad?
os.getenv only supports strings as the first argument (key).
If the provided argument is not a string, os.getenv will throw a
TypeError at runtime.
## Example
```
os.getenv(1)
```
## Use instead:
```
os.getenv("1")
```
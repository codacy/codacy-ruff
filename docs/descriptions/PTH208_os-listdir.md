# os-listdir (PTH208)
Derived from the flake8-use-pathlib linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of os.listdir.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using pathlib's
Path.iterdir() can improve readability over os.listdir().
## Example
```
p = "."
for d in os.listdir(p):
    ...
if os.listdir(p):
    ...
if "file" in os.listdir(p):
    ...
```
## Use instead:
```
p = Path(".")
for d in p.iterdir():
    ...
if any(p.iterdir()):
    ...
if (p / "file").exists():
    ...
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```
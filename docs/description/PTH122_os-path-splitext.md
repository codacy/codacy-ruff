# os-path-splitext (PTH122)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.splitext.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path. When possible, using Path object
methods such as Path.suffix and Path.stem can improve readability over
the os.path module's counterparts (e.g., os.path.splitext()).
os.path.splitext() specifically returns a tuple of the file root and
extension (e.g., given splitext('/foo/bar.py'), os.path.splitext()
returns ("foo/bar", ".py"). These outputs can be reconstructed through a
combination of Path.suffix (".py"), Path.stem ("bar"), and
Path.parent ("foo").
## Examples
```
import os
(root, ext) = os.path.splitext("foo/bar.py")
```
## Use instead:
```
from pathlib import Path
path = Path("foo/bar.py")
root = path.parent / path.stem
ext = path.suffix
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```
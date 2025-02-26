# glob (PTH207)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for the use of glob.glob() and glob.iglob().
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os and glob.
When possible, using Path object methods such as Path.glob() can
improve readability over their low-level counterparts (e.g.,
glob.glob()).
Note that glob.glob() and Path.glob() are not exact equivalents:
glob-module functions
Path.glob()
Hidden files
Hidden files are excluded by default. On Python 3.11+, the include_hidden keyword can be used to include hidden directories.
Includes hidden files by default.
Eagerness
glob.iglob() returns a lazy iterator. Under the hood, glob.glob() simply converts the iterator to a list.
Path.glob() returns a lazy iterator.
Working directory
glob.glob() and glob.iglob() take a root_dir keyword to set the current working directory.
Path.rglob() can be used to return the relative path.
Globstar (**)
The recursive flag must be set to True for the ** pattern to match any files and zero or more directories, subdirectories, and symbolic links.
The ** pattern in Path.glob() means "this directory and all subdirectories, recursively". In other words, it enables recursive globbing.
## Example
```
import glob
import os
glob.glob(os.path.join("my_path", "requirements*.txt"))
```
## Use instead:
```
from pathlib import Path
Path("my_path").glob("requirements*.txt")
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```
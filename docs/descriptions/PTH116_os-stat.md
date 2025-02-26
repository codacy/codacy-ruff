# os-stat (PTH116)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.stat.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using Path object
methods such as Path.stat() can improve readability over the os
module's counterparts (e.g., os.path.stat()).
## Examples
```
import os
from pwd import getpwuid
from grp import getgrgid
stat = os.stat(file_name)
owner_name = getpwuid(stat.st_uid).pw_name
group_name = getgrgid(stat.st_gid).gr_name
```
## Use instead:
```
from pathlib import Path
file_path = Path(file_name)
stat = file_path.stat()
owner_name = file_path.owner()
group_name = file_path.group()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```
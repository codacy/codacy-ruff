# manual-from-import (PLR0402)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for submodule imports that are aliased to the submodule name.
## Why is this bad?
Using the from keyword to import the submodule is more concise and
readable.
## Example
```
import concurrent.futures as futures
```
## Use instead:
```
from concurrent import futures
```
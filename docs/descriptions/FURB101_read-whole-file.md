# read-whole-file (FURB101)
Derived from the refurb linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of open and read that can be replaced by pathlib
methods, like Path.read_text and Path.read_bytes.
## Why is this bad?
When reading the entire contents of a file into a variable, it's simpler
and more concise to use pathlib methods like Path.read_text and
Path.read_bytes instead of open and read calls via with statements.
## Example
```
with open(filename) as f:
    contents = f.read()
```
## Use instead:
```
from pathlib import Path
contents = Path(filename).read_text()
```
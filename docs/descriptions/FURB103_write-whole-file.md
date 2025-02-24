# write-whole-file (FURB103)
Derived from the refurb linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of open and write that can be replaced by pathlib
methods, like Path.write_text and Path.write_bytes.
## Why is this bad?
When writing a single string to a file, it's simpler and more concise
to use pathlib methods like Path.write_text and Path.write_bytes
instead of open and write calls via with statements.
## Example
```
with open(filename, "w") as f:
    f.write(contents)
```
## Use instead:
```
from pathlib import Path
Path(filename).write_text(contents)
```
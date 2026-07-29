# write-whole-file (FURB103)
Preview (since v0.3.6) ·
Related issues ·
View source
Derived from the refurb linter.
Fix is sometimes available.
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
with open("file.txt", "w") as f:
    f.write("some text")
```
## Use instead:
```
from pathlib import Path
Path("file.txt").write_text("some text")
Fix Safety
This rule's fix is marked as unsafe if the replacement would remove comments attached to the original expression.
```
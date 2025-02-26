# line-contains-hack (FIX004)
Derived from the flake8-fixme linter.
## What it does
Checks for "HACK" comments.
## Why is this bad?
"HACK" comments are used to describe an issue that should be resolved
(usually, a suboptimal solution or temporary workaround).
Consider resolving the issue before deploying the code.
Note that if you use "HACK" comments as a form of documentation, this
rule may not be appropriate for your project.
## Example
```
import os
def running_windows():  # HACK: Use platform module instead.
    try:
        os.mkdir("C:\\Windows\\System32\\")
    except FileExistsError:
        return True
    else:
        os.rmdir("C:\\Windows\\System32\\")
        return False
```
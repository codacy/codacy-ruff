# assignment-to-os-environ (B003)
Derived from the flake8-bugbear linter.
## What it does
Checks for assignments to os.environ.
## Why is this bad?
In Python, os.environ is a mapping that represents the environment of the
current process.
However, reassigning to os.environ does not clear the environment. Instead,
it merely updates the os.environ for the current process. This can lead to
unexpected behavior, especially when running the program in a subprocess.
Instead, use os.environ.clear() to clear the environment, or use the
env argument of subprocess.Popen to pass a custom environment to
a subprocess.
## Example
```
import os
os.environ = {"foo": "bar"}
```
## Use instead:
```
import os
os.environ.clear()
os.environ["foo"] = "bar"
```
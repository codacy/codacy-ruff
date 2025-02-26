# invalid-envvar-default (PLW1508)
Derived from the Pylint linter.
## What it does
Checks for os.getenv calls with invalid default values.
## Why is this bad?
If an environment variable is set, os.getenv will return its value as
a string. If the environment variable is not set, os.getenv will
return None, or the default value if one is provided.
If the default value is not a string or None, then it will be
inconsistent with the return type of os.getenv, which can lead to
confusing behavior.
## Example
```
import os
int(os.getenv("FOO", 1))
```
## Use instead:
```
import os
int(os.getenv("FOO", "1"))
```
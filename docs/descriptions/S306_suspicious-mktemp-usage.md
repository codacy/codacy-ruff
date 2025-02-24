# suspicious-mktemp-usage (S306)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of tempfile.mktemp.
## Why is this bad?
tempfile.mktemp returns a pathname of a file that does not exist at the
time the call is made; then, the caller is responsible for creating the
file and subsequently using it. This is insecure because another process
could create a file with the same name between the time the function
returns and the time the caller creates the file.
tempfile.mktemp is deprecated in favor of tempfile.mkstemp which
creates the file when it is called. Consider using tempfile.mkstemp
instead, either directly or via a context manager such as
tempfile.TemporaryFile.
In preview, this rule will also flag references to tempfile.mktemp.
## Example
```
import tempfile
tmp_file = tempfile.mktemp()
with open(tmp_file, "w") as file:
    file.write("Hello, world!")
```
## Use instead:
```
import tempfile
with tempfile.TemporaryFile() as file:
    file.write("Hello, world!")
```
# hardcoded-temp-file (S108)
Derived from the flake8-bandit linter.
## What it does
Checks for the use of hardcoded temporary file or directory paths.
## Why is this bad?
The use of hardcoded paths for temporary files can be insecure. If an
attacker discovers the location of a hardcoded path, they can replace the
contents of the file or directory with a malicious payload.
Other programs may also read or write contents to these hardcoded paths,
causing unexpected behavior.
## Example
```
with open("/tmp/foo.txt", "w") as file:
    ...
```
## Use instead:
```
import tempfile
with tempfile.NamedTemporaryFile() as file:
    ...
```
# tarfile-unsafe-members (S202)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of tarfile.extractall.
## Why is this bad?
Extracting archives from untrusted sources without prior inspection is
a security risk, as maliciously crafted archives may contain files that
will be written outside of the target directory. For example, the archive
could include files with absolute paths (e.g., /etc/passwd), or relative
paths with parent directory references (e.g., ../etc/passwd).
On Python 3.12 and later, use filter='data' to prevent the most dangerous
security issues (see: PEP 706). On earlier versions, set the members
argument to a trusted subset of the archive's members.
## Example
```
import tarfile
import tempfile
tar = tarfile.open(filename)
tar.extractall(path=tempfile.mkdtemp())
tar.close()
```
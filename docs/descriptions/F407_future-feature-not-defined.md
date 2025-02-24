# future-feature-not-defined (F407)
Derived from the Pyflakes linter.
## What it does
Checks for __future__ imports that are not defined in the current Python
version.
## Why is this bad?
Importing undefined or unsupported members from the __future__ module is
a SyntaxError.
```
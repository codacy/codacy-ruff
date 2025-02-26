# non-ascii-import-name (PLC2403)
Derived from the Pylint linter.
## What it does
Checks for the use of non-ASCII characters in import statements.
## Why is this bad?
The use of non-ASCII characters in import statements can cause confusion
and compatibility issues (see: PEP 672).
## Example
```
import bár
```
## Use instead:
```
import bar
If the module is third-party, use an ASCII-only alias:
import bár as bar
```
# redefined-while-unused (F811)
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for variable definitions that redefine (or "shadow") unused
variables.
## Why is this bad?
Redefinitions of unused names are unnecessary and often indicative of a
mistake.
## Example
```
import foo
import bar
import foo  # Redefinition of unused `foo` from line 1
```
## Use instead:
```
import foo
import bar
```
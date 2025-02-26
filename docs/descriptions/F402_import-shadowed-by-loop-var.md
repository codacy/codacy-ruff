# import-shadowed-by-loop-var (F402)
Derived from the Pyflakes linter.
## What it does
Checks for import bindings that are shadowed by loop variables.
## Why is this bad?
Shadowing an import with loop variables makes the code harder to read and
reason about, as the identify of the imported binding is no longer clear.
It's also often indicative of a mistake, as it's unlikely that the loop
variable is intended to be used as the imported binding.
Consider using a different name for the loop variable.
## Example
```
from os import path
for path in files:
    print(path)
```
## Use instead:
```
from os import path
for filename in files:
    print(filename)
```
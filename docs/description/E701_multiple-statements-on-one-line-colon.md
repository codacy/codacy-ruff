# multiple-statements-on-one-line-colon (E701)
Added in v0.0.245 ·
Related issues ·
View source
Derived from the pycodestyle linter.
## What it does
Checks for compound statements (multiple statements on the same line).
## Why is this bad?
According to PEP 8, "compound statements are generally discouraged".
## Example
```
if foo == "blah": do_blah_thing()
```
## Use instead:
```
if foo == "blah":
    do_blah_thing()
```
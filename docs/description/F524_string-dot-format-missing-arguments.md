# string-dot-format-missing-arguments (F524)
Added in v0.0.139 ·
Related issues ·
View source
Derived from the Pyflakes linter.
## What it does
Checks for str.format calls with placeholders that are missing arguments.
## Why is this bad?
In str.format calls, omitting arguments for placeholders will raise a
KeyError at runtime.
## Example
```
"{greeting}, {name}".format(name="World")
```
## Use instead:
```
"{greeting}, {name}".format(greeting="Hello", name="World")
```
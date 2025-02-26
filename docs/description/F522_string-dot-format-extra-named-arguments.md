# string-dot-format-extra-named-arguments (F522)
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for str.format calls with unused keyword arguments.
## Why is this bad?
Unused keyword arguments are redundant, and often indicative of a mistake.
They should be removed.
## Example
```
"Hello, {name}".format(greeting="Hello", name="World")
```
## Use instead:
```
"Hello, {name}".format(name="World")
```
# string-dot-format-mixing-automatic (F525)
Derived from the Pyflakes linter.
## What it does
Checks for str.format calls that mix automatic and manual numbering.
## Why is this bad?
In str.format calls, mixing automatic and manual numbering will raise a
ValueError at runtime.
## Example
```
"{0}, {}".format("Hello", "World")
```
## Use instead:
```
"{0}, {1}".format("Hello", "World")
Or:
"{}, {}".format("Hello", "World")
```
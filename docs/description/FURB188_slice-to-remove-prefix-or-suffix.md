# slice-to-remove-prefix-or-suffix (FURB188)
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for code that could be written more idiomatically using
str.removeprefix()
or str.removesuffix().
Specifically, the rule flags code that conditionally removes a prefix or suffix
using a slice operation following an if test that uses str.startswith() or str.endswith().
The rule is only applied if your project targets Python 3.9 or later.
## Why is this bad?
The methods str.removeprefix()
and str.removesuffix(),
introduced in Python 3.9, have the same behavior while being more readable and efficient.
## Example
```
def example(filename: str, text: str):
    filename = filename[:-4] if filename.endswith(".txt") else filename
    if text.startswith("pre"):
        text = text[3:]
```
## Use instead:
```
def example(filename: str, text: str):
    filename = filename.removesuffix(".txt")
    text = text.removeprefix("pre")
```
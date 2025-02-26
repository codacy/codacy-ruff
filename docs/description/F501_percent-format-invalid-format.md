# percent-format-invalid-format (F501)
Derived from the Pyflakes linter.
## What it does
Checks for invalid printf-style format strings.
## Why is this bad?
Conversion specifiers are required for printf-style format strings. These
specifiers must contain a % character followed by a conversion type.
## Example
```
"Hello, %" % "world"
```
## Use instead:
```
"Hello, %s" % "world"
```
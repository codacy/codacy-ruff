# percent-format-unsupported-format-character (F509)
Derived from the Pyflakes linter.
## What it does
Checks for printf-style format strings with invalid format characters.
## Why is this bad?
In printf-style format strings, the % character is used to indicate
placeholders. If a % character is not followed by a valid format
character, it will raise a ValueError at runtime.
## Example
```
"Hello, %S" % "world"
```
## Use instead:
```
"Hello, %s" % "world"
```
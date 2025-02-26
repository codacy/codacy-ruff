# percent-format-positional-count-mismatch (F507)
Derived from the Pyflakes linter.
## What it does
Checks for printf-style format strings that have a mismatch between the
number of positional placeholders and the number of substitution values.
## Why is this bad?
When a printf-style format string is provided with too many or too few
substitution values, it will raise a TypeError at runtime.
## Example
```
"%s, %s" % ("Hello", "world", "!")
```
## Use instead:
```
"%s, %s" % ("Hello", "world")
```
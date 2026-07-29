# f-string-percent-format (RUF073)
Preview (since 0.15.8) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of the % operator on f-strings.
## Why is this bad?
F-strings already support interpolation via {...} expressions.
Using the % operator on an f-string is almost certainly a mistake,
since the f-string's interpolation and %-formatting serve the same
purpose. This typically indicates that the developer intended to use
either an f-string or %-formatting, but not both.
## Example
```
f"{name}" % name
f"hello %s %s" % (first, second)
```
## Use instead:
```
f"{name}"
f"hello {first} {second}"
```
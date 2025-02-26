# f-string-missing-placeholders (F541)
Derived from the Pyflakes linter.
Fix is always available.
## What it does
Checks for f-strings that do not contain any placeholder expressions.
## Why is this bad?
f-strings are a convenient way to format strings, but they are not
necessary if there are no placeholder expressions to format. In this
case, a regular string should be used instead, as an f-string without
placeholders can be confusing for readers, who may expect such a
placeholder to be present.
An f-string without any placeholders could also indicate that the
author forgot to add a placeholder expression.
## Example
```
f"Hello, world!"
```
## Use instead:
```
"Hello, world!"
Note: to maintain compatibility with PyFlakes, this rule only flags
f-strings that are part of an implicit concatenation if none of the
f-string segments contain placeholder expressions.
For example:
# Will not be flagged.
(
    f"Hello,"
    f" {name}!"
)
# Will be flagged.
(
    f"Hello,"
    f" World!"
)
See #10885 for more.
```
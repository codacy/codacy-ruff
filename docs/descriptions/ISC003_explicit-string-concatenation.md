# explicit-string-concatenation (ISC003)
Derived from the flake8-implicit-str-concat linter.
## What it does
Checks for string literals that are explicitly concatenated (using the
+ operator).
## Why is this bad?
For string literals that wrap across multiple lines, implicit string
concatenation within parentheses is preferred over explicit
concatenation using the + operator, as the former is more readable.
## Example
```
z = (
    "The quick brown fox jumps over the lazy "
    + "dog"
)
```
## Use instead:
```
z = (
    "The quick brown fox jumps over the lazy "
    "dog"
)
```
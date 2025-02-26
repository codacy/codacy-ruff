# multi-line-implicit-string-concatenation (ISC002)
Derived from the flake8-implicit-str-concat linter.
## What it does
Checks for implicitly concatenated strings that span multiple lines.
## Why is this bad?
For string literals that wrap across multiple lines, PEP 8 recommends
the use of implicit string concatenation within parentheses instead of
using a backslash for line continuation, as the former is more readable
than the latter.
By default, this rule will only trigger if the string literal is
concatenated via a backslash. To disallow implicit string concatenation
altogether, set the lint.flake8-implicit-str-concat.allow-multiline option
to false.
## Example
```
z = "The quick brown fox jumps over the lazy "\
    "dog."
```
## Use instead:
```
z = (
    "The quick brown fox jumps over the lazy "
    "dog."
)
```
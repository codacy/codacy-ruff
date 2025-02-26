# single-line-implicit-string-concatenation (ISC001)
Derived from the flake8-implicit-str-concat linter.
Fix is sometimes available.
## What it does
Checks for implicitly concatenated strings on a single line.
## Why is this bad?
While it is valid Python syntax to concatenate multiple string or byte
literals implicitly (via whitespace delimiters), it is unnecessary and
negatively affects code readability.
In some cases, the implicit concatenation may also be unintentional, as
code formatters are capable of introducing single-line implicit
concatenations when collapsing long lines.
## Example
```
z = "The quick " "brown fox."
```
## Use instead:
```
z = "The quick brown fox."
```
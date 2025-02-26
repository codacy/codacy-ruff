# unnecessary-escaped-quote (Q004)
Derived from the flake8-quotes linter.
Fix is always available.
## What it does
Checks for strings that include unnecessarily escaped quotes.
## Why is this bad?
If a string contains an escaped quote that doesn't match the quote
character used for the string, it's unnecessary and can be removed.
## Example
```
foo = "bar\'s"
```
## Use instead:
```
foo = "bar's"
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter automatically removes unnecessary escapes, making the rule
redundant.
```
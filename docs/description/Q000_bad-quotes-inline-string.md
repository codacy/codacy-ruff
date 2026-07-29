# bad-quotes-inline-string (Q000)
Added in v0.0.88 ·
Related issues ·
View source
Derived from the flake8-quotes linter.
Fix is sometimes available.
## What it does
Checks for inline strings that use single quotes or double quotes,
depending on the value of the lint.flake8-quotes.inline-quotes option.
## Why is this bad?
Consistency is good. Use either single or double quotes for inline
strings, but be consistent.
## Example
```
foo = 'bar'
Assuming inline-quotes is set to double, use instead:
foo = "bar"
```
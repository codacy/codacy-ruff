# prohibited-trailing-comma (COM819)
Added in v0.0.223 ·
Related issues ·
View source
Derived from the flake8-commas linter.
Fix is always available.
## What it does
Checks for the presence of prohibited trailing commas.
## Why is this bad?
Trailing commas are not essential in some cases and can therefore be viewed
as unnecessary.
## Example
```
foo = (1, 2, 3,)
```
## Use instead:
```
foo = (1, 2, 3)
Formatter compatibility
We recommend against using this rule alongside the formatter. With the
default format.skip-magic-trailing-comma = false, trailing commas can be
intentional: the formatter treats them as a signal to preserve multiline
formatting. When set to true, the formatter removes those trailing commas
where possible, making this rule redundant.
```
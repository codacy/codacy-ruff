# prohibited-trailing-comma (COM819)
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
We recommend against using this rule alongside the formatter. The
formatter enforces consistent use of trailing commas, making the rule redundant.
```
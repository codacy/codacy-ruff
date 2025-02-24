# missing-whitespace-around-bitwise-or-shift-operator (E227)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace around bitwise and shift operators.
## Why is this bad?
According to PEP 8, there should be one space before and after bitwise and
shift operators (\<<, >>, &, |, ^).
## Example
```
x = 128<<1
```
## Use instead:
```
x = 128 << 1
```
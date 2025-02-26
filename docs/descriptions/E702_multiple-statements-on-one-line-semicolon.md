# multiple-statements-on-one-line-semicolon (E702)
Derived from the pycodestyle linter.
## What it does
Checks for multiline statements on one line.
## Why is this bad?
According to PEP 8, including multi-clause statements on the same line is
discouraged.
## Example
```
do_one(); do_two(); do_three()
```
## Use instead:
```
do_one()
do_two()
do_three()
```
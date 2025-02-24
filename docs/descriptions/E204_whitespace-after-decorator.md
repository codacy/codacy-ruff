# whitespace-after-decorator (E204)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for trailing whitespace after a decorator's opening @.
## Why is this bad?
Including whitespace after the @ symbol is not compliant with
PEP 8.
## Example
```
@ decorator
def func():
   pass
```
## Use instead:
```
@decorator
def func():
  pass
```
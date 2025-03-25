# type-none-comparison (FURB169)
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for uses of type that compare the type of an object to the type of None.
## Why is this bad?
There is only ever one instance of None, so it is more efficient and
readable to use the is operator to check if an object is None.
## Example
```
type(obj) is type(None)
```
## Use instead:
```
obj is None
Fix safety
If the fix might remove comments, it will be marked as unsafe.
```
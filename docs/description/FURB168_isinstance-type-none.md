# isinstance-type-none (FURB168)
Added in 0.5.0 ·
Related issues ·
View source
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for uses of isinstance that check if an object is of type None.
## Why is this bad?
There is only ever one instance of None, so it is more efficient and
readable to use the is operator to check if an object is None.
## Example
```
isinstance(obj, type(None))
```
## Use instead:
```
obj is None
Fix safety
The fix will be marked as unsafe if there are any comments within the call.
```
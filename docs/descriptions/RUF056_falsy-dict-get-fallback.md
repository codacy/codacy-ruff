# falsy-dict-get-fallback (RUF056)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for dict.get(key, falsy_value) calls in boolean test positions.
## Why is this bad?
The default fallback None is already falsy.
## Example
```
if dict.get(key, False):
    ...
```
## Use instead:
```
if dict.get(key):
    ...
Fix safety
This rule's fix is marked as safe, unless the dict.get() call contains comments between arguments.
```
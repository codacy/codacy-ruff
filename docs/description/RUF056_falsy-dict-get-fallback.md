# falsy-dict-get-fallback (RUF056)
Preview (since 0.8.5) ·
Related issues ·
View source
Fix is sometimes available.
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
This rule's fix is marked as safe, unless the dict.get() call contains comments between
arguments that will be deleted.
Fix availability
This rule's fix is unavailable in cases where invalid arguments are provided to dict.get. As
shown in the documentation, dict.get takes two positional-only arguments, so invalid cases
are identified by the presence of more than two arguments or any keyword arguments.
```
# starmap-zip (RUF058)
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for itertools.starmap calls where the second argument is a zip call.
## Why is this bad?
zip-ping iterables only to unpack them later from within starmap is unnecessary.
For such cases, map() should be used instead.
## Example
```
from itertools import starmap
starmap(func, zip(a, b))
starmap(func, zip(a, b, strict=True))
```
## Use instead:
```
map(func, a, b)
map(func, a, b, strict=True)  # 3.14+
Fix safety
This rule's fix is marked as unsafe if the starmap or zip expressions contain comments that
would be deleted by applying the fix. Otherwise, the fix can be applied safely.
Fix availability
This rule will emit a diagnostic but not suggest a fix if map has been shadowed from its
builtin binding.
```
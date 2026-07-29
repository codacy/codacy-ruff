# invalid-rule-code (RUF102)
Added in 0.15.0 ·
Related issues ·
View source
Fix is always available.
## What it does
Checks for noqa codes that are invalid.
## Why is this bad?
Invalid rule codes serve no purpose and may indicate outdated code suppressions.
## Example
```
import os  # noqa: XYZ999
```
## Use instead:
```
import os
Or if there are still valid codes needed:
import os  # noqa: E402
Fix safety
The rule's fix is marked as unsafe when a full suppression comment would be removed and there
are other nested comments on the same line. Removing such a comment can change the behavior of
other suppression comments before or after the removed comment.
```
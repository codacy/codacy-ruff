# regex-flag-alias (FURB167)
Added in 0.5.0 ·
Related issues ·
View source
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for the use of shorthand aliases for regular expression flags
(e.g., re.I instead of re.IGNORECASE).
## Why is this bad?
The regular expression module provides descriptive names for each flag,
along with single-letter aliases. Prefer the descriptive names, as they
are more readable and self-documenting.
## Example
```
import re
if re.search("^hello", "hello world", re.I):
    ...
```
## Use instead:
```
import re
if re.search("^hello", "hello world", re.IGNORECASE):
    ...
```
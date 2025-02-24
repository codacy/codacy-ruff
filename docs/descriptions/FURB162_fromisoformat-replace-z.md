# fromisoformat-replace-z (FURB162)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for datetime.fromisoformat() calls
where the only argument is an inline replacement
of Z with a zero offset timezone.
## Why is this bad?
On Python 3.11 and later, datetime.fromisoformat() can handle most ISO 8601
formats including ones affixed with Z, so such an operation is unnecessary.
More information on unsupported formats
can be found in the official documentation.
## Example
```
from datetime import datetime
date = "2025-01-01T00:00:00Z"
datetime.fromisoformat(date.replace("Z", "+00:00"))
datetime.fromisoformat(date[:-1] + "-00")
datetime.fromisoformat(date.strip("Z", "-0000"))
datetime.fromisoformat(date.rstrip("Z", "-00:00"))
```
## Use instead:
```
from datetime import datetime
date = "2025-01-01T00:00:00Z"
datetime.fromisoformat(date)
Fix safety
The fix is always marked as unsafe,
as it might change the program's behaviour.
For example, working code might become non-working:
d = "Z2025-01-01T00:00:00Z"  # Note the leading `Z`
datetime.fromisoformat(d.strip("Z") + "+00:00")  # Fine
datetime.fromisoformat(d)  # Runtime error
```
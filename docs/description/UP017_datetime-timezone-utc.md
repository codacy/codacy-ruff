# datetime-timezone-utc (UP017)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for uses of datetime.timezone.utc.
## Why is this bad?
As of Python 3.11, datetime.UTC is an alias for datetime.timezone.utc.
The alias is more readable and generally preferred over the full path.
## Example
```
import datetime
datetime.timezone.utc
```
## Use instead:
```
import datetime
datetime.UTC
```
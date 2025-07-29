# datetime-min-max (DTZ901)
Derived from the flake8-datetimez linter.
## What it does
Checks for uses of datetime.datetime.min and datetime.datetime.max.
## Why is this bad?
datetime.min and datetime.max are non-timezone-aware datetime objects.
As such, operations on datetime.min and datetime.max may behave
unexpectedly, as in:
import datetime
# Timezone: UTC-14
datetime.datetime.min.timestamp()  # ValueError: year 0 is out of range
datetime.datetime.max.timestamp()  # ValueError: year 10000 is out of range
## Example
```
import datetime
datetime.datetime.max
```
## Use instead:
```
import datetime
datetime.datetime.max.replace(tzinfo=datetime.UTC)
```
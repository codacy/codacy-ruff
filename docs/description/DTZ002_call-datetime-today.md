# call-datetime-today (DTZ002)
Added in v0.0.188 ·
Related issues ·
View source
Derived from the flake8-datetimez linter.
## What it does
Checks for usage of datetime.datetime.today().
## Why is this bad?
datetime objects are "naive" by default, in that they do not include
timezone information. "Naive" objects are easy to understand, but ignore
some aspects of reality, which can lead to subtle bugs. Timezone-aware
datetime objects are preferred, as they represent a specific moment in
time, unlike "naive" objects.
datetime.datetime.today() creates a "naive" object; instead, use
datetime.datetime.now(tz=...) to create a timezone-aware object.
The name today() can be misleading, because it suggests a calendar date,
but it actually returns the current local date and time as a datetime.
That can make intent harder to infer when reading code.
## Example
```
import datetime
datetime.datetime.today()
```
## Use instead:
```
import datetime
datetime.datetime.now(tz=datetime.timezone.utc)
Or, for Python 3.11 and later:
import datetime
datetime.datetime.now(tz=datetime.UTC)
```
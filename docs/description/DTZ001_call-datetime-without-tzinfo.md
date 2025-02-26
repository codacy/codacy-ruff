# call-datetime-without-tzinfo (DTZ001)
Derived from the flake8-datetimez linter.
## What it does
Checks for datetime instantiations that do not specify a timezone.
## Why is this bad?
datetime objects are "naive" by default, in that they do not include
timezone information. "Naive" objects are easy to understand, but ignore
some aspects of reality, which can lead to subtle bugs. Timezone-aware
datetime objects are preferred, as they represent a specific moment in
time, unlike "naive" objects.
By providing a non-None value for tzinfo, a datetime can be made
timezone-aware.
## Example
```
import datetime
datetime.datetime(2000, 1, 1, 0, 0, 0)
```
## Use instead:
```
import datetime
datetime.datetime(2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
Or, on Python 3.11 and later:
import datetime
datetime.datetime(2000, 1, 1, 0, 0, 0, tzinfo=datetime.UTC)
```
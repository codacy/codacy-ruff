# call-date-fromtimestamp (DTZ012)
Derived from the flake8-datetimez linter.
## What it does
Checks for usage of datetime.date.fromtimestamp().
## Why is this bad?
Python datetime objects can be naive or timezone-aware. While an aware
object represents a specific moment in time, a naive object does not
contain enough information to unambiguously locate itself relative to other
datetime objects. Since this can lead to errors, it is recommended to
always use timezone-aware objects.
datetime.date.fromtimestamp(ts) returns a naive datetime object.
Instead, use datetime.datetime.fromtimestamp(ts, tz=...) to create a
timezone-aware object.
## Example
```
import datetime
datetime.date.fromtimestamp(946684800)
```
## Use instead:
```
import datetime
datetime.datetime.fromtimestamp(946684800, tz=datetime.timezone.utc)
Or, for Python 3.11 and later:
import datetime
datetime.datetime.fromtimestamp(946684800, tz=datetime.UTC)
```
# call-datetime-utcfromtimestamp (DTZ004)
Derived from the flake8-datetimez linter.
## What it does
Checks for usage of datetime.datetime.utcfromtimestamp().
## Why is this bad?
Python datetime objects can be naive or timezone-aware. While an aware
object represents a specific moment in time, a naive object does not
contain enough information to unambiguously locate itself relative to other
datetime objects. Since this can lead to errors, it is recommended to
always use timezone-aware objects.
datetime.datetime.utcfromtimestamp() returns a naive datetime
object; instead, use datetime.datetime.fromtimestamp(ts, tz=...)
to create a timezone-aware object.
## Example
```
import datetime
datetime.datetime.utcfromtimestamp(946684800)
```
## Use instead:
```
import datetime
datetime.datetime.fromtimestamp(946684800, tz=datetime.timezone.utc)
Or, on Python 3.11 and later:
import datetime
datetime.datetime.fromtimestamp(946684800, tz=datetime.UTC)
```
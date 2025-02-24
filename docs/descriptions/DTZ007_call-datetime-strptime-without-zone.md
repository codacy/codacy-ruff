# call-datetime-strptime-without-zone (DTZ007)
Derived from the flake8-datetimez linter.
## What it does
Checks for uses of datetime.datetime.strptime() that lead to naive
datetime objects.
## Why is this bad?
Python datetime objects can be naive or timezone-aware. While an aware
object represents a specific moment in time, a naive object does not
contain enough information to unambiguously locate itself relative to other
datetime objects. Since this can lead to errors, it is recommended to
always use timezone-aware objects.
datetime.datetime.strptime() without %z returns a naive datetime
object. Follow it with .replace(tzinfo=<timezone>) or .astimezone().
## Example
```
import datetime
datetime.datetime.strptime("2022/01/31", "%Y/%m/%d")
Instead, use .replace(tzinfo=<timezone>):
import datetime
datetime.datetime.strptime("2022/01/31", "%Y/%m/%d").replace(
    tzinfo=datetime.timezone.utc
)
Or, use .astimezone():
import datetime
datetime.datetime.strptime("2022/01/31", "%Y/%m/%d").astimezone(datetime.timezone.utc)
On Python 3.11 and later, datetime.timezone.utc can be replaced with
datetime.UTC.
```
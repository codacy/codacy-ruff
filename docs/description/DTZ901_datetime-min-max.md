# datetime-min-max (DTZ901)
Derived from the flake8-datetimez linter.
## What it does
Checks for uses of datetime.datetime.min and datetime.datetime.max.
## Why is this bad?
datetime.min and datetime.max are non-timezone-aware datetime objects.
As such, operations on datetime.min and datetime.max may behave
unexpectedly, as in:
# Timezone: UTC-14
datetime.min.timestamp()  # ValueError: year 0 is out of range
datetime.max.timestamp()  # ValueError: year 10000 is out of range
## Example
```
datetime.max
```
## Use instead:
```
datetime.max.replace(tzinfo=datetime.UTC)
```
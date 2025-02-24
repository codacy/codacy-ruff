# datetime-min-max (DTZ901)
Derived from the flake8-datetimez linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of datetime.datetime.max and datetime.datetime.min.
## Why is this bad?
datetime.max and datetime.min are non-timezone-aware datetime objects.
As such, operations on datetime.max and datetime.min may behave
unexpectedly, as in:
# Timezone: UTC-14
datetime.max.timestamp()  # ValueError: year 10000 is out of range
datetime.min.timestamp()  # ValueError: year 0 is out of range
## Example
```
datetime.max
```
## Use instead:
```
datetime.max.replace(tzinfo=datetime.UTC)
```
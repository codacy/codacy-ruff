# airflow3-removal (AIR302)
Derived from the Airflow linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of deprecated Airflow functions and values.
## Why is this bad?
Airflow 3.0 removed various deprecated functions, members, and other
values. Some have more modern replacements. Others are considered too niche
and not worth to be maintained in Airflow.
## Example
```
from airflow.utils.dates import days_ago
yesterday = days_ago(today, 1)
```
## Use instead:
```
from datetime import timedelta
yesterday = today - timedelta(days=1)
```
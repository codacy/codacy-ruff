# airflow3-removal (AIR301)
Added in 0.13.0 ·
Related issues ·
View source
Derived from the Airflow linter.
Fix is sometimes available.
## What it does
Checks for uses of deprecated Airflow functions and values.
## Why is this bad?
Airflow 3.0 removed various deprecated functions, members, and other
values. Some have more modern replacements. Others are considered too niche
and not worth continued maintenance in Airflow.
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
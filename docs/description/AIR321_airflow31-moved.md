# airflow31-moved (AIR321)
Preview (since 0.15.1) ·
Related issues ·
View source
Derived from the Airflow linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of deprecated or moved Airflow functions and values in Airflow 3.1.
## Why is this bad?
Airflow 3.1 deprecated or moved various functions, members, and other values.
## Example
```
from airflow.utils.timezone import convert_to_utc
from datetime import datetime
convert_to_utc(datetime.now())
```
## Use instead:
```
from airflow.sdk.timezone import convert_to_utc
from datetime import datetime
convert_to_utc(datetime.now())
```
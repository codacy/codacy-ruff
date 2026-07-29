# airflow3-suggested-update (AIR311)
Added in 0.13.0 ·
Related issues ·
View source
Derived from the Airflow linter.
Fix is sometimes available.
## What it does
Checks for uses of deprecated Airflow functions and values that still have
a compatibility layer.
## Why is this bad?
Airflow 3.0 removed various deprecated functions, members, and other
values. Some have more modern replacements. Others are considered too niche
and not worth continued maintenance in Airflow.
Even though these symbols still work fine on Airflow 3.0, they are expected to be removed in a future version.
Where available, users should replace the removed functionality with the new alternatives.
## Example
```
from airflow import Dataset
Dataset(uri="test://test/")
```
## Use instead:
```
from airflow.sdk import Asset
Asset(uri="test://test/")
```
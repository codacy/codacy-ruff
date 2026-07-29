# airflow3-moved-to-provider (AIR302)
Added in 0.13.0 ·
Related issues ·
View source
Derived from the Airflow linter.
Fix is sometimes available.
## What it does
Checks for uses of Airflow functions and values that have been moved to its providers
(e.g., apache-airflow-providers-fab).
## Why is this bad?
Airflow 3.0 moved various deprecated functions, members, and other
values to its providers. The user needs to install the corresponding provider and replace
the original usage with the one in the provider.
## Example
```
from airflow.auth.managers.fab.fab_auth_manager import FabAuthManager
fab_auth_manager_app = FabAuthManager().get_fastapi_app()
```
## Use instead:
```
from airflow.providers.fab.auth_manager.fab_auth_manager import FabAuthManager
fab_auth_manager_app = FabAuthManager().get_fastapi_app()
```
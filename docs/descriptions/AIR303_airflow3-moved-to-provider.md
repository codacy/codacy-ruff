# airflow3-moved-to-provider (AIR303)
Derived from the Airflow linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of Airflow functions and values that have been moved to it providers.
(e.g., apache-airflow-providers-fab)
## Why is this bad?
Airflow 3.0 moved various deprecated functions, members, and other
values to its providers. The user needs to install the corresponding provider and replace
the original usage with the one in the provider
## Example
```
from airflow.auth.managers.fab.fab_auth_manage import FabAuthManager
```
## Use instead:
```
from airflow.providers.fab.auth_manager.fab_auth_manage import FabAuthManager
```
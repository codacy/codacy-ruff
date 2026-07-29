# airflow3-dag-dynamic-value (AIR304)
Preview (since 0.15.6) ·
Related issues ·
View source
Derived from the Airflow linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for calls to runtime-varying functions (such as datetime.now())
used as arguments in Airflow Dag or task constructors.
## Why is this bad?
Using runtime-varying values as arguments to Dag or task constructors
causes the serialized Dag hash to change on every parse, creating
infinite Dag versions in the dag_version and serialized_dag tables.
This leads to unbounded database growth and can eventually cause
out-of-memory conditions.
## Example
```
from datetime import datetime
from airflow import DAG
dag = DAG(dag_id="my_dag", start_date=datetime.now())
```
## Use instead:
```
from datetime import datetime
from airflow import DAG
dag = DAG(dag_id="my_dag", start_date=datetime(2024, 1, 1))
```
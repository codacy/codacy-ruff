# airflow-variable-name-task-id-mismatch (AIR001)
Derived from the Airflow linter.
## What it does
Checks that the task variable name matches the task_id value for
Airflow Operators.
## Why is this bad?
When initializing an Airflow Operator, for consistency, the variable
name should match the task_id value. This makes it easier to
follow the flow of the DAG.
## Example
```
from airflow.operators import PythonOperator
incorrect_name = PythonOperator(task_id="my_task")
```
## Use instead:
```
from airflow.operators import PythonOperator
my_task = PythonOperator(task_id="my_task")
```
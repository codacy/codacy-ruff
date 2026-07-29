# airflow-task-branch-as-short-circuit (AIR004)
Preview (since 0.15.12) ·
Related issues ·
View source
Derived from the Airflow linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for branching logic that could be replaced with a short-circuit
pattern, either via @task.branch decorated functions or
BranchPythonOperator callables.
## Why is this bad?
When a branch function has at least two return statements and exactly
one of them returns a non-empty list, the function is effectively acting
as a short-circuit operator. Using @task.short_circuit or
ShortCircuitOperator is simpler and more readable in such cases.
## Example
```
Using the TaskFlow API:
from airflow.decorators import task
@task.branch
def my_task():
    if condition:
        return ["my_downstream_task"]
    return []
```
## Use instead:
```
from airflow.decorators import task
@task.short_circuit
def my_task():
    return condition
Using the standard operator API:
from airflow.operators.python import BranchPythonOperator
def my_callable():
    if condition:
        return ["my_downstream_task"]
    return []
task = BranchPythonOperator(task_id="my_task", python_callable=my_callable)
```
## Use instead:
```
from airflow.operators.python import ShortCircuitOperator
def my_callable():
    return condition
task = ShortCircuitOperator(task_id="my_task", python_callable=my_callable)
```
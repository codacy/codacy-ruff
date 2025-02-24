# airflow-dag-no-schedule-argument (AIR301)
Derived from the Airflow linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for a DAG() class or @dag() decorator without an explicit
schedule parameter.
## Why is this bad?
The default schedule value on Airflow 2 is timedelta(days=1), which is
almost never what a user is looking for. Airflow 3 changes this the default
to None, and would break existing DAGs using the implicit default.
If your DAG does not have an explicit schedule argument, Airflow 2
schedules a run for it every day (at the time determined by start_date).
Such a DAG will no longer be scheduled on Airflow 3 at all, without any
exceptions or other messages visible to the user.
## Example
```
from airflow import DAG
# Using the implicit default schedule.
dag = DAG(dag_id="my_dag")
```
## Use instead:
```
from datetime import timedelta
from airflow import DAG
dag = DAG(dag_id="my_dag", schedule=timedelta(days=1))
```
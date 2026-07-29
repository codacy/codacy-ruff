# airflow-dag-no-schedule-argument (AIR002)
Added in 0.13.0 ·
Related issues ·
View source
Derived from the Airflow linter.
## What it does
Checks for a DAG() class or @dag() decorator without an explicit
schedule (or schedule_interval for Airflow 1) parameter.
## Why is this bad?
The default value of the schedule parameter on Airflow 2 and
schedule_interval on Airflow 1 is timedelta(days=1), which is almost
never what a user is looking for. Airflow 3 changed the default value to None,
and would break existing Dags using the implicit default.
If your Dag does not have an explicit schedule / schedule_interval argument,
Airflow 2 schedules a run for it every day (at the time determined by start_date).
Such a Dag will no longer be scheduled on Airflow 3 at all, without any
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
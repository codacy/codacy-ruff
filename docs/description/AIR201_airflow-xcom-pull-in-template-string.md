# airflow-xcom-pull-in-template-string (AIR201)
Preview (since 0.15.11) ·
Related issues ·
View source
Derived from the Airflow linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for Airflow operator keyword arguments that use a Jinja template
string containing a single xcom_pull call to retrieve another task's
output.
## Why is this bad?
Using {{ ti.xcom_pull(task_ids='some_task') }} as a string template to
access the output of an upstream task is less readable and more
error-prone than using the .output attribute on the task object
directly. The .output attribute provides better IDE support and makes
task dependencies more explicit.
## Example
```
from airflow.operators.python import PythonOperator
task_1 = PythonOperator(task_id="task_1", python_callable=my_func)
task_2 = PythonOperator(
    task_id="task_2",
    op_args="{{ ti.xcom_pull(task_ids='task_1') }}",
)
```
## Use instead:
```
from airflow.operators.python import PythonOperator
task_1 = PythonOperator(task_id="task_1", python_callable=my_func)
task_2 = PythonOperator(
    task_id="task_2",
    op_args=task_1.output,
)
Fix safety
The fix is always unsafe because the variable in scope that matches the
task ID may not be the Airflow task object that produced the XCom value.
```
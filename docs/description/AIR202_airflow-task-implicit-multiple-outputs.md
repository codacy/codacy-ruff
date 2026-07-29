# airflow-task-implicit-multiple-outputs (AIR202)
Preview (since 0.15.14) ·
Related issues ·
View source
Derived from the Airflow linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for @task-decorated functions whose multiple_outputs behavior is
determined by Airflow's runtime inference rather than being set explicitly.
## Why is this bad?
At runtime, Airflow infers multiple_outputs from the return type
annotation: if it resolves to a subclass of collections.abc.Mapping, the
return value is split into one XCom per key; otherwise it is stored as a
single XCom. This couples typing to XCom layout in a non-obvious way —
renaming, removing, or refining the return annotation silently changes the
Dag's XCom behavior.
Passing multiple_outputs= explicitly makes the author's intent clear,
insulates the Dag from future changes to inference, and increases
awareness of the parameter.
## Example
```
from airflow.sdk import task
@task
def extract() -> dict:
    return {"x": 1, "y": 2}
```
## Use instead:
```
from airflow.sdk import task
@task(multiple_outputs=True)
def extract() -> dict:
    return {"x": 1, "y": 2}
Fix safety
The fix is always marked unsafe: the inserted value mirrors Airflow's
current inference (True when the return annotation is a Mapping
subclass, False otherwise), but the author may have intended a different
XCom layout, and a function with multiple return paths may not always
return a dict.
```
# start-process-with-no-shell (S606)
Derived from the flake8-bandit linter.
## What it does
Checks for functions that start a process without a shell.
## Why is this bad?
Invoking any kind of external executable via a function call can pose
security risks if arbitrary variables are passed to the executable, or if
the input is otherwise unsanitised or unvalidated.
This rule specifically flags functions in the os module that spawn
subprocesses without the use of a shell. Note that these typically pose a
much smaller security risk than subprocesses that are started with a
shell, which are flagged by start-process-with-a-shell (S605).
This gives you the option of enabling one rule while disabling the other
if you decide that the security risk from these functions is acceptable
for your use case.
## Example
```
import os
def insecure_function(arbitrary_user_input: str):
    os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", arbitrary_user_input)
```
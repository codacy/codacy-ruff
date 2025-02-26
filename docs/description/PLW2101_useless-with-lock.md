# useless-with-lock (PLW2101)
Derived from the Pylint linter.
## What it does
Checks for lock objects that are created and immediately discarded in
with statements.
## Why is this bad?
Creating a lock (via threading.Lock or similar) in a with statement
has no effect, as locks are only relevant when shared between threads.
Instead, assign the lock to a variable outside the with statement,
and share that variable between threads.
## Example
```
import threading
counter = 0
def increment():
    global counter
    with threading.Lock():
        counter += 1
```
## Use instead:
```
import threading
counter = 0
lock = threading.Lock()
def increment():
    global counter
    with lock:
        counter += 1
```
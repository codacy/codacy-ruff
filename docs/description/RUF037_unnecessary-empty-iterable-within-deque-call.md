# unnecessary-empty-iterable-within-deque-call (RUF037)
Added in 0.15.0 ·
Related issues ·
View source
Fix is sometimes available.
## What it does
Checks for use of collections.deque with an empty iterable as the first argument.
## Why is this bad?
It's unnecessary to use an empty literal as a deque's iterable, since this is already the default behavior.
## Example
```
from collections import deque
queue = deque(set())
queue = deque([], 10)
```
## Use instead:
```
from collections import deque
queue = deque()
queue = deque(maxlen=10)
Fix safety
The fix is marked as unsafe whenever it would delete comments present in the deque call or if
there are unrecognized arguments other than iterable and maxlen.
Fix availability
This rule's fix is unavailable if any starred arguments are present after the initial iterable.
```
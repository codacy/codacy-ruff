# unnecessary-empty-iterable-within-deque-call (RUF037)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for usages of collections.deque that have an empty iterable as the first argument.
## Why is this bad?
It's unnecessary to use an empty literal as a deque's iterable, since this is already the default behavior.
## Examples
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
```
# reuse-of-groupby-generator (B031)
Derived from the flake8-bugbear linter.
## What it does
Checks for multiple usage of the generator returned from
itertools.groupby().
## Why is this bad?
Using the generator more than once will do nothing on the second usage.
If that data is needed later, it should be stored as a list.
Examples:
import itertools
for name, group in itertools.groupby(data):
    for _ in range(5):
        do_something_with_the_group(group)
```
## Use instead:
```
import itertools
for name, group in itertools.groupby(data):
    values = list(group)
    for _ in range(5):
        do_something_with_the_group(values)
```
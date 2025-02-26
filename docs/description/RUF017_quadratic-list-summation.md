# quadratic-list-summation (RUF017)
Fix is always available.
## What it does
Checks for the use of sum() to flatten lists of lists, which has
quadratic complexity.
## Why is this bad?
The use of sum() to flatten lists of lists is quadratic in the number of
lists, as sum() creates a new list for each element in the summation.
Instead, consider using another method of flattening lists to avoid
quadratic complexity. The following methods are all linear in the number of
lists:
functools.reduce(operator.iadd, lists, [])
list(itertools.chain.from_iterable(lists))
[item for sublist in lists for item in sublist]
When fixing relevant violations, Ruff defaults to the functools.reduce
form, which outperforms the other methods in microbenchmarks.
## Example
```
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
joined = sum(lists, [])
```
## Use instead:
```
import functools
import operator
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
functools.reduce(operator.iadd, lists, [])
```
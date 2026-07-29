# quadratic-list-summation (RUF017)
Added in v0.0.285 ·
Related issues ·
View source
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
[*sublist for sublist in lists] (Python 3.15+)
functools.reduce(operator.iadd, lists, [])
list(itertools.chain.from_iterable(lists))
[item for sublist in lists for item in sublist]
When fixing relevant violations, Ruff uses the starred-list-comprehension
form on Python 3.15 and later. On older Python versions, Ruff falls back to
the functools.reduce form, which outperforms the other pre-3.15
alternatives in microbenchmarks.
## Example
```
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
joined = sum(lists, [])
On Python 3.14 and earlier, use instead:
import functools
import operator
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
joined = functools.reduce(operator.iadd, lists, [])
On Python 3.15 and later, use instead:
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
joined = [*sublist for sublist in lists]
Fix safety
This fix is always marked as unsafe because the replacement may accept any
iterable where sum previously required lists. On Python 3.15 and later,
Ruff uses iterable unpacking within a list comprehension; on older Python
versions, Ruff uses operator.iadd. In both cases, code that previously
raised an error may silently succeed. Moreover, the fix could remove
comments from the original code.
```
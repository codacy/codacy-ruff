# zip-instead-of-pairwise (RUF007)
Fix is sometimes available.
## What it does
Checks for use of zip() to iterate over successive pairs of elements.
## Why is this bad?
When iterating over successive pairs of elements, prefer
itertools.pairwise() over zip().
itertools.pairwise() is more readable and conveys the intent of the code
more clearly.
## Example
```
letters = "ABCD"
zip(letters, letters[1:])  # ("A", "B"), ("B", "C"), ("C", "D")
```
## Use instead:
```
from itertools import pairwise
letters = "ABCD"
pairwise(letters)  # ("A", "B"), ("B", "C"), ("C", "D")
```
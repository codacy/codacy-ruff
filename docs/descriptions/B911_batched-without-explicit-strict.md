# batched-without-explicit-strict (B911)
Derived from the flake8-bugbear linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for itertools.batched calls without an explicit strict parameter.
## Why is this bad?
By default, if the length of the iterable is not divisible by
the second argument to itertools.batched, the last batch
will be shorter than the rest.
In Python 3.13, a strict parameter was added which allows controlling if the batches must be of uniform length.
Pass strict=True to raise a ValueError if the batches are of non-uniform length.
Otherwise, pass strict=False to make the intention explicit.
## Example
```
itertools.batched(iterable, n)
Use instead if the batches must be of uniform length:
itertools.batched(iterable, n, strict=True)
Or if the batches can be of non-uniform length:
itertools.batched(iterable, n, strict=False)
Known deviations
Unlike the upstream B911, this rule will not report infinite iterators
(e.g., itertools.cycle(...)).
```
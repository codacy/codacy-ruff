# manual-list-comprehension (PERF401)
Derived from the Perflint linter.
Fix is sometimes available.
## What it does
Checks for for loops that can be replaced by a list comprehension.
## Why is this bad?
When creating a transformed list from an existing list using a for-loop,
prefer a list comprehension. List comprehensions are more readable and
more performant.
Using the below as an example, the list comprehension is ~10% faster on
Python 3.11, and ~25% faster on Python 3.10.
Note that, as with all perflint rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.
## Example
```
original = list(range(10000))
filtered = []
for i in original:
    if i % 2:
        filtered.append(i)
```
## Use instead:
```
original = list(range(10000))
filtered = [x for x in original if x % 2]
If you're appending to an existing list, use the extend method instead:
original = list(range(10000))
filtered.extend(x for x in original if x % 2)
Take care that if the original for-loop uses an assignment expression
as a conditional, such as if match:=re.match("\d+","123"), then
the corresponding comprehension must wrap the assignment
expression in parentheses to avoid a syntax error.
```
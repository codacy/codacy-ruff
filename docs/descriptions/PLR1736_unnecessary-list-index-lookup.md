# unnecessary-list-index-lookup (PLR1736)
Derived from the Pylint linter.
Fix is always available.
## What it does
Checks for index-based list accesses during enumerate iterations.
## Why is this bad?
When iterating over a list with enumerate, the current item is already
available alongside its index. Using the index to look up the item is
unnecessary.
## Example
```
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(letters[index])
```
## Use instead:
```
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(letter)
```
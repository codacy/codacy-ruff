# print-empty-string (FURB105)
Added in 0.5.0 ·
Related issues ·
View source
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for print calls with unnecessary empty strings as positional
arguments and unnecessary sep keyword arguments.
## Why is this bad?
Prefer calling print without any positional arguments, which is
equivalent and more concise.
Similarly, when printing one or fewer items, the sep keyword argument,
(used to define the string that separates the print arguments) can be
omitted, as it's redundant when there are no items to separate.
## Example
```
print("")
```
## Use instead:
```
print()
Fix safety
This fix is marked as unsafe if it removes comments or an unused sep keyword argument
that is not known to be a valid separator. Removing such arguments may change the
program's behavior by skipping their evaluation or hiding a TypeError.
```
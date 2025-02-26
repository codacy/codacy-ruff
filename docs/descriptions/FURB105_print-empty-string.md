# print-empty-string (FURB105)
Derived from the refurb linter.
Fix is sometimes available.
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
```
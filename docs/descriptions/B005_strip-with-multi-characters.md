# strip-with-multi-characters (B005)
Derived from the flake8-bugbear linter.
## What it does
Checks for uses of multi-character strings in .strip(), .lstrip(), and
.rstrip() calls.
## Why is this bad?
All characters in the call to .strip(), .lstrip(), or .rstrip() are
removed from the leading and trailing ends of the string. If the string
contains multiple characters, the reader may be misled into thinking that
a prefix or suffix is being removed, rather than a set of characters.
In Python 3.9 and later, you can use str.removeprefix and
str.removesuffix to remove an exact prefix or suffix from a string,
respectively, which should be preferred when possible.
Known problems
As a heuristic, this rule only flags multi-character strings that contain
duplicate characters. This allows usages like .strip("xyz"), which
removes all occurrences of the characters x, y, and z from the
leading and trailing ends of the string, but not .strip("foo").
The use of unique, multi-character strings may be intentional and
consistent with the intent of .strip(), .lstrip(), or .rstrip(),
while the use of duplicate-character strings is very likely to be a
mistake.
## Example
```
"text.txt".strip(".txt")  # "e"
```
## Use instead:
```
"text.txt".removesuffix(".txt")  # "text"
```
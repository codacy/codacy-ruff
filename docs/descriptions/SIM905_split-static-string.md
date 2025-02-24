# split-static-string (SIM905)
Derived from the flake8-simplify linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for static str.split calls that can be replaced with list literals.
## Why is this bad?
List literals are more readable and do not require the overhead of calling str.split.
## Example
```
"a,b,c,d".split(",")
```
## Use instead:
```
["a", "b", "c", "d"]
Fix safety
This rule's fix is marked as unsafe for implicit string concatenations with comments interleaved
between segments, as comments may be removed.
For example, the fix would be marked as unsafe in the following case:
(
    "a"  # comment
    ","  # comment
    "b"  # comment
).split(",")
```
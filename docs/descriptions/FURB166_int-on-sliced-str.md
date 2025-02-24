# int-on-sliced-str (FURB166)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of int with an explicit base in which a string expression
is stripped of its leading prefix (i.e., 0b, 0o, or 0x).
## Why is this bad?
Given an integer string with a prefix (e.g., 0xABC), Python can automatically
determine the base of the integer by the prefix without needing to specify
it explicitly.
Instead of int(num[2:], 16), use int(num, 0), which will automatically
deduce the base based on the prefix.
## Example
```
num = "0xABC"
if num.startswith("0b"):
    i = int(num[2:], 2)
elif num.startswith("0o"):
    i = int(num[2:], 8)
elif num.startswith("0x"):
    i = int(num[2:], 16)
print(i)
```
## Use instead:
```
num = "0xABC"
i = int(num, 0)
print(i)
Fix safety
The rule's fix is marked as unsafe, as Ruff cannot guarantee that the
argument to int will remain valid when its base is included in the
function call.
```
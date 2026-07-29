# implicit-string-concatenation-in-collection-literal (ISC004)
Added in 0.16.0 ·
Related issues ·
View source
Derived from the flake8-implicit-str-concat linter.
Fix is always available.
## What it does
Checks for implicitly concatenated strings inside list, tuple, and set literals.
## Why is this bad?
In collection literals, implicit string concatenation is often the result of
a missing comma between elements, which can silently merge items together.
## Example
```
facts = (
    "Lobsters have blue blood.",
    "The liver is the only human organ that can fully regenerate itself.",
    "Clarinets are made almost entirely out of wood from the mpingo tree."
    "In 1971, astronaut Alan Shepard played golf on the moon.",
)
Instead, you likely intended:
facts = (
    "Lobsters have blue blood.",
    "The liver is the only human organ that can fully regenerate itself.",
    "Clarinets are made almost entirely out of wood from the mpingo tree.",
    "In 1971, astronaut Alan Shepard played golf on the moon.",
)
If the concatenation is intentional, wrap it in parentheses to make it
explicit:
facts = (
    "Lobsters have blue blood.",
    "The liver is the only human organ that can fully regenerate itself.",
    (
        "Clarinets are made almost entirely out of wood from the mpingo tree."
        "In 1971, astronaut Alan Shepard played golf on the moon."
    ),
)
Fix safety
The fix is safe in that it does not change the semantics of your code.
However, the issue is that you may often want to change semantics
by adding a missing comma. Thus, the fix is always marked as unsafe.
```
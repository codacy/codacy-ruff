# rule-codes-in-suppression-comments (RUF106)
Preview (since 0.15.22) ·
Related issues ·
View source
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for rule codes in Ruff-specific suppression comments.
## Why is this bad?
Human-readable rule names are easier to understand than rule codes. Using names also avoids
requiring readers to look up the meaning of each code.
This rule applies to ruff: ignore, ruff: file-ignore, ruff: disable, and ruff: enable
comments.
## Example
```
import os  # ruff: ignore[F401]
```
## Use instead:
```
import os  # ruff: ignore[unused-import]
```
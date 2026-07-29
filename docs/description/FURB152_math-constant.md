# math-constant (FURB152)
Preview (since v0.1.6) ·
Related issues ·
View source
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for literals that are similar to constants in math module.
## Why is this bad?
Hard-coding mathematical constants like π increases code duplication,
reduces readability, and may lead to a lack of precision.
## Example
```
A = 3.141592 * r**2
```
## Use instead:
```
A = math.pi * r**2
```
# rule-codes-in-selectors (RUF201)
Preview (since 0.15.22) ·
Related issues ·
View source
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for any configuration files that use rule codes as selectors.
## Why is this bad?
Human-readable rule names are easier to understand than rule codes. Using names also avoids
requiring readers to look up the meaning of each code.
## Example
```
[tool.ruff.lint]
select = ["F401"]
```
## Use instead:
```
[tool.ruff.lint]
select = ["unused-import"]
```
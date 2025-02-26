# redirected-noqa (RUF101)
Fix is always available.
## What it does
Checks for noqa directives that use redirected rule codes.
## Why is this bad?
When one of Ruff's rule codes has been redirected, the implication is that the rule has
been deprecated in favor of another rule or code. To keep your codebase
consistent and up-to-date, prefer the canonical rule code over the deprecated
code.
## Example
```
x = eval(command)  # noqa: PGH001
```
## Use instead:
```
x = eval(command)  # noqa: S307
```
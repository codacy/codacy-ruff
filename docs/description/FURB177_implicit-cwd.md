# implicit-cwd (FURB177)
Derived from the refurb linter.
Fix is sometimes available.
## What it does
Checks for current-directory lookups using Path().resolve().
## Why is this bad?
When looking up the current directory, prefer Path.cwd() over
Path().resolve(), as Path.cwd() is more explicit in its intent.
## Example
```
cwd = Path().resolve()
```
## Use instead:
```
cwd = Path.cwd()
```
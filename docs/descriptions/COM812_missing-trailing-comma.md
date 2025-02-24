# missing-trailing-comma (COM812)
Derived from the flake8-commas linter.
Fix is always available.
## What it does
Checks for the absence of trailing commas.
## Why is this bad?
The presence of a trailing comma can reduce diff size when parameters or
elements are added or removed from function calls, function definitions,
literals, etc.
## Example
```
foo = {
    "bar": 1,
    "baz": 2
}
```
## Use instead:
```
foo = {
    "bar": 1,
    "baz": 2,
}
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter enforces consistent use of trailing commas, making the rule redundant.
```
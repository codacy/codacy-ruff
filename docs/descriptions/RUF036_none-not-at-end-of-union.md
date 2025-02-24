# none-not-at-end-of-union (RUF036)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for type annotations where None is not at the end of an union.
## Why is this bad?
Type annotation unions are associative, meaning that the order of the elements
does not matter. The None literal represents the absence of a value. For
readability, it's preferred to write the more informative type expressions first.
## Example
```
def func(arg: None | int): ...
```
## Use instead:
```
def func(arg: int | None): ...
```
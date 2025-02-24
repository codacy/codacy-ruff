# named-expr-without-context (PLW0131)
Derived from the Pylint linter.
## What it does
Checks for uses of named expressions (e.g., a := 42) that can be
replaced by regular assignment statements (e.g., a = 42).
## Why is this bad?
While a top-level named expression is syntactically and semantically valid,
it's less clear than a regular assignment statement. Named expressions are
intended to be used in comprehensions and generator expressions, where
assignment statements are not allowed.
## Example
```
(a := 42)
```
## Use instead:
```
a = 42
```
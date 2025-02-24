# percent-format-extra-named-arguments (F504)
Derived from the Pyflakes linter.
Fix is always available.
## What it does
Checks for unused mapping keys in printf-style format strings.
## Why is this bad?
Unused named placeholders in printf-style format strings are unnecessary,
and likely indicative of a mistake. They should be removed.
## Example
```
"Hello, %(name)s" % {"greeting": "Hello", "name": "World"}
```
## Use instead:
```
"Hello, %(name)s" % {"name": "World"}
```
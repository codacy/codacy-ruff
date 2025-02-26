# percent-format-mixed-positional-and-named (F506)
Derived from the Pyflakes linter.
## What it does
Checks for printf-style format strings that have mixed positional and
named placeholders.
## Why is this bad?
Python does not support mixing positional and named placeholders in
printf-style format strings. The use of mixed placeholders will raise a
TypeError at runtime.
## Example
```
"%s, %(name)s" % ("Hello", {"name": "World"})
```
## Use instead:
```
"%s, %s" % ("Hello", "World")
Or:
"%(greeting)s, %(name)s" % {"greeting": "Hello", "name": "World"}
```
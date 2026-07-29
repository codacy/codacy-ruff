# percent-format-expected-mapping (F502)
Added in v0.0.142 ·
Related issues ·
View source
Derived from the Pyflakes linter.
## What it does
Checks for named placeholders in printf-style format strings without
mapping-type values.
## Why is this bad?
When using named placeholders in printf-style format strings, the values
must be a map type (such as a dictionary). Otherwise, the expression will
raise a TypeError.
## Example
```
"%(greeting)s, %(name)s" % ("Hello", "World")
```
## Use instead:
```
"%(greeting)s, %(name)s" % {"greeting": "Hello", "name": "World"}
Or:
"%s, %s" % ("Hello", "World")
```
# percent-format-expected-sequence (F503)
Derived from the Pyflakes linter.
## What it does
Checks for uses of mapping-type values in printf-style format strings
without named placeholders.
## Why is this bad?
When using mapping-type values (such as dict) in printf-style format
strings, the keys must be named. Otherwise, the expression will raise a
TypeError.
## Example
```
"%s, %s" % {"greeting": "Hello", "name": "World"}
```
## Use instead:
```
"%(greeting)s, %(name)s" % {"greeting": "Hello", "name": "World"}
Or:
"%s, %s" % ("Hello", "World")
```
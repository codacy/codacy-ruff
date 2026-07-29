# percent-format-missing-argument (F505)
Added in v0.0.142 ·
Related issues ·
View source
Derived from the Pyflakes linter.
## What it does
Checks for named placeholders in printf-style format strings that are not
present in the provided mapping.
## Why is this bad?
Named placeholders that lack a corresponding value in the provided mapping
will raise a KeyError.
## Example
```
"%(greeting)s, %(name)s" % {"name": "world"}
```
## Use instead:
```
"Hello, %(name)s" % {"name": "world"}
```
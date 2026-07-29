# mako-templates (S702)
Added in v0.2.0 ·
Related issues ·
View source
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the mako templates.
## Why is this bad?
Mako templates allow HTML and JavaScript rendering by default, and are
inherently open to XSS attacks. Ensure variables in all templates are
properly escaped via the h (HTML) or x (XML) filters, depending on
context. For example, to HTML escape the variable data, use ${ data |h }.
## Example
```
from mako.template import Template
Template("${ data }")  # Unescaped: vulnerable to XSS.
```
## Use instead:
```
from mako.template import Template
Template("${ data |h }")  # HTML-escaped with the `h` filter.
```
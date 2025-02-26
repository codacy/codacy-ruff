# mako-templates (S702)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the mako templates.
## Why is this bad?
Mako templates allow HTML and JavaScript rendering by default, and are
inherently open to XSS attacks. Ensure variables in all templates are
properly sanitized via the n, h or x flags (depending on context).
For example, to HTML escape the variable data, use ${ data |h }.
## Example
```
from mako.template import Template
Template("hello")
```
## Use instead:
```
from mako.template import Template
Template("hello |h")
```
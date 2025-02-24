# jinja2-autoescape-false (S701)
Derived from the flake8-bandit linter.
## What it does
Checks for jinja2 templates that use autoescape=False.
## Why is this bad?
jinja2 templates that use autoescape=False are vulnerable to cross-site
scripting (XSS) attacks that allow attackers to execute arbitrary
JavaScript.
By default, jinja2 sets autoescape to False, so it is important to
set autoescape=True or use the select_autoescape function to mitigate
XSS vulnerabilities.
## Example
```
import jinja2
jinja2.Environment(loader=jinja2.FileSystemLoader("."))
```
## Use instead:
```
import jinja2
jinja2.Environment(loader=jinja2.FileSystemLoader("."), autoescape=True)
```
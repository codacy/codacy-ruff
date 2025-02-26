# suspicious-mark-safe-usage (S308)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of calls to django.utils.safestring.mark_safe.
## Why is this bad?
Cross-site scripting (XSS) vulnerabilities allow attackers to execute
arbitrary JavaScript. To guard against XSS attacks, Django templates
assumes that data is unsafe and automatically escapes malicious strings
before rending them.
django.utils.safestring.mark_safe marks a string as safe for use in HTML
templates, bypassing XSS protection. This is dangerous because it may allow
cross-site scripting attacks if the string is not properly escaped.
In preview, this rule will also flag references to django.utils.safestring.mark_safe.
## Example
```
from django.utils.safestring import mark_safe
content = mark_safe("<script>alert('Hello, world!')</script>")  # XSS.
```
## Use instead:
```
content = "<script>alert('Hello, world!')</script>"  # Safe if rendered.
```
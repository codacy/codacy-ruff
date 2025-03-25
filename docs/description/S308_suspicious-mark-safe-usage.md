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
templates, bypassing XSS protection. Its usage can be dangerous if the
contents of the string are dynamically generated, because it may allow
cross-site scripting attacks if the string is not properly escaped.
For dynamically generated strings, consider utilizing
django.utils.html.format_html.
In preview, this rule will also flag references to django.utils.safestring.mark_safe.
## Example
```
from django.utils.safestring import mark_safe
def render_username(username):
    return mark_safe(f"<i>{username}</i>")  # Dangerous if username is user-provided.
```
## Use instead:
```
from django.utils.html import format_html
def render_username(username):
    return django.utils.html.format_html("<i>{}</i>", username)  # username is escaped.
```
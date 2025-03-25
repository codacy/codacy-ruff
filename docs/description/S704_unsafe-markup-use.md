# unsafe-markup-use (S704)
Derived from the flake8-bandit linter.
## What it does
Checks for non-literal strings being passed to markupsafe.Markup.
## Why is this bad?
[markupsafe.Markup][markupsafe.Markup] does not perform any escaping, so passing dynamic
content, like f-strings, variables or interpolated strings will potentially
lead to XSS vulnerabilities.
Instead you should interpolate the Markup object.
Using lint.flake8-bandit.extend-markup-names additional objects can be
treated like Markup.
This rule was originally inspired by flake8-markupsafe but doesn't carve
out any exceptions for i18n related calls by default.
You can use lint.flake8-bandit.allowed-markup-calls to specify exceptions.
## Example
```
Given:
from markupsafe import Markup
content = "<script>alert('Hello, world!')</script>"
html = Markup(f"<b>{content}</b>")  # XSS
```
## Use instead:
```
from markupsafe import Markup
content = "<script>alert('Hello, world!')</script>"
html = Markup("<b>{}</b>").format(content)  # Safe
Given:
from markupsafe import Markup
lines = [
    Markup("<b>heading</b>"),
    "<script>alert('XSS attempt')</script>",
]
html = Markup("<br>".join(lines))  # XSS
```
## Use instead:
```
from markupsafe import Markup
lines = [
    Markup("<b>heading</b>"),
    "<script>alert('XSS attempt')</script>",
]
html = Markup("<br>").join(lines)  # Safe
```
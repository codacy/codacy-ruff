# suspicious-httpoxy-import (S412)
Preview (since v0.1.12) ·
Related issues ·
View source
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of wsgiref.handlers.CGIHandler and
twisted.web.twcgi.CGIScript.
## Why is this bad?
httpoxy is a set of vulnerabilities that affect application code running in
CGI or CGI-like environments. The use of CGI for web applications should be
avoided to prevent this class of attack.
## Example
```
from wsgiref.handlers import CGIHandler
```
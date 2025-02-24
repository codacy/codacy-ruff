# request-with-no-cert-validation (S501)
Derived from the flake8-bandit linter.
## What it does
Checks for HTTPS requests that disable SSL certificate checks.
## Why is this bad?
If SSL certificates are not verified, an attacker could perform a "man in
the middle" attack by intercepting and modifying traffic between the client
and server.
## Example
```
import requests
requests.get("https://www.example.com", verify=False)
```
## Use instead:
```
import requests
requests.get("https://www.example.com")  # By default, `verify=True`.
```
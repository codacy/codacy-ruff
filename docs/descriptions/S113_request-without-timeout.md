# request-without-timeout (S113)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the Python requests or httpx module that omit the
timeout parameter.
## Why is this bad?
The timeout parameter is used to set the maximum time to wait for a
response from the server. By omitting the timeout parameter, the program
may hang indefinitely while awaiting a response.
## Example
```
import requests
requests.get("https://www.example.com/")
```
## Use instead:
```
import requests
requests.get("https://www.example.com/", timeout=10)
```
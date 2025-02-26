# suspicious-url-open-usage (S310)
Derived from the flake8-bandit linter.
## What it does
Checks for instances where URL open functions are used with unexpected schemes.
## Why is this bad?
Some URL open functions allow the use of file: or custom schemes (for use
instead of http: or https:). An attacker may be able to use these
schemes to access or modify unauthorized resources, and cause unexpected
behavior.
To mitigate this risk, audit all uses of URL open functions and ensure that
only permitted schemes are used (e.g., allowing http: and https:, and
disallowing file: and ftp:).
In preview, this rule will also flag references to URL open functions.
## Example
```
from urllib.request import urlopen
url = input("Enter a URL: ")
with urlopen(url) as response:
    ...
```
## Use instead:
```
from urllib.request import urlopen
url = input("Enter a URL: ")
if not url.startswith(("http:", "https:")):
    raise ValueError("URL must start with 'http:' or 'https:'")
with urlopen(url) as response:
    ...
```
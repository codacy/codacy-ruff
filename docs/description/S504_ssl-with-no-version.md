# ssl-with-no-version (S504)
Added in v0.2.0 ·
Related issues ·
View source
Derived from the flake8-bandit linter.
## What it does
Checks for calls to ssl.wrap_socket() without an ssl_version.
## Why is this bad?
This method is known to provide a default value that maximizes
compatibility, but permits use of insecure protocols.
## Example
```
import ssl
ssl.wrap_socket()
```
## Use instead:
```
import ssl
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1_2)
```
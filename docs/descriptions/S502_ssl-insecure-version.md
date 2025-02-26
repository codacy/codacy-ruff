# ssl-insecure-version (S502)
Derived from the flake8-bandit linter.
## What it does
Checks for function calls with parameters that indicate the use of insecure
SSL and TLS protocol versions.
## Why is this bad?
Several highly publicized exploitable flaws have been discovered in all
versions of SSL and early versions of TLS. The following versions are
considered insecure, and should be avoided:
SSL v2
SSL v3
TLS v1
TLS v1.1
This method supports detection on the Python's built-in ssl module and
the pyOpenSSL module.
## Example
```
import ssl
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1)
```
## Use instead:
```
import ssl
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1_2)
```
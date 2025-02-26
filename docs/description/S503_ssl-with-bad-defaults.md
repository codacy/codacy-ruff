# ssl-with-bad-defaults (S503)
Derived from the flake8-bandit linter.
## What it does
Checks for function definitions with default arguments set to insecure SSL
and TLS protocol versions.
## Why is this bad?
Several highly publicized exploitable flaws have been discovered in all
versions of SSL and early versions of TLS. The following versions are
considered insecure, and should be avoided:
SSL v2
SSL v3
TLS v1
TLS v1.1
## Example
```
import ssl
def func(version=ssl.PROTOCOL_TLSv1): ...
```
## Use instead:
```
import ssl
def func(version=ssl.PROTOCOL_TLSv1_2): ...
```
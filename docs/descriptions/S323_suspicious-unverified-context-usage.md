# suspicious-unverified-context-usage (S323)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of ssl._create_unverified_context.
## Why is this bad?
PEP 476 enabled certificate and hostname validation by default in Python
standard library HTTP clients. Previously, Python did not validate
certificates by default, which could allow an attacker to perform a "man in
the middle" attack by intercepting and modifying traffic between client and
server.
To support legacy environments, ssl._create_unverified_context reverts to
the previous behavior that does perform verification. Otherwise, use
ssl.create_default_context to create a secure context.
In preview, this rule will also flag references to ssl._create_unverified_context.
## Example
```
import ssl
context = ssl._create_unverified_context()
```
## Use instead:
```
import ssl
context = ssl.create_default_context()
```
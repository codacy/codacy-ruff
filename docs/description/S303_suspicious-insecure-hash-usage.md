# suspicious-insecure-hash-usage (S303)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of weak or broken cryptographic hash functions.
## Why is this bad?
Weak or broken cryptographic hash functions may be susceptible to
collision attacks (where two different inputs produce the same hash) or
pre-image attacks (where an attacker can find an input that produces a
given hash). This can lead to security vulnerabilities in applications
that rely on these hash functions.
Avoid using weak or broken cryptographic hash functions in security
contexts. Instead, use a known secure hash function such as SHA-256.
In preview, this rule will also flag references to insecure hash functions.
## Example
```
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.MD5())
digest.update(b"Hello, world!")
digest.finalize()
```
## Use instead:
```
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256())
digest.update(b"Hello, world!")
digest.finalize()
```
# hashlib-insecure-hash-function (S324)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of weak or broken cryptographic hash functions in
hashlib and crypt libraries.
## Why is this bad?
Weak or broken cryptographic hash functions may be susceptible to
collision attacks (where two different inputs produce the same hash) or
pre-image attacks (where an attacker can find an input that produces a
given hash). This can lead to security vulnerabilities in applications
that rely on these hash functions.
Avoid using weak or broken cryptographic hash functions in security
contexts. Instead, use a known secure hash function such as SHA256.
## Example
```
import hashlib
def certificate_is_valid(certificate: bytes, known_hash: str) -> bool:
    hash = hashlib.md5(certificate).hexdigest()
    return hash == known_hash
```
## Use instead:
```
import hashlib
def certificate_is_valid(certificate: bytes, known_hash: str) -> bool:
    hash = hashlib.sha256(certificate).hexdigest()
    return hash == known_hash
or add usedforsecurity=False if the hashing algorithm is not used in a security context, e.g.
as a non-cryptographic one-way compression function:
import hashlib
def certificate_is_valid(certificate: bytes, known_hash: str) -> bool:
    hash = hashlib.md5(certificate, usedforsecurity=False).hexdigest()
    return hash == known_hash
```
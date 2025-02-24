# suspicious-insecure-cipher-usage (S304)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of weak or broken cryptographic ciphers.
## Why is this bad?
Weak or broken cryptographic ciphers may be susceptible to attacks that
allow an attacker to decrypt ciphertext without knowing the key or
otherwise compromise the security of the cipher, such as forgeries.
Use strong, modern cryptographic ciphers instead of weak or broken ones.
In preview, this rule will also flag references to insecure ciphers.
## Example
```
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=None)
encryptor = cipher.encryptor()
```
## Use instead:
```
from cryptography.fernet import Fernet
fernet = Fernet(key)
```
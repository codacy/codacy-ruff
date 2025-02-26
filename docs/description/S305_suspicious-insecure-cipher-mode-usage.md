# suspicious-insecure-cipher-mode-usage (S305)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of weak or broken cryptographic cipher modes.
## Why is this bad?
Weak or broken cryptographic ciphers may be susceptible to attacks that
allow an attacker to decrypt ciphertext without knowing the key or
otherwise compromise the security of the cipher, such as forgeries.
Use strong, modern cryptographic ciphers instead of weak or broken ones.
In preview, this rule will also flag references to insecure cipher modes.
## Example
```
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=modes.ECB(iv))
encryptor = cipher.encryptor()
```
## Use instead:
```
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=modes.CTR(iv))
encryptor = cipher.encryptor()
```
# weak-cryptographic-key (S505)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of cryptographic keys with vulnerable key sizes.
## Why is this bad?
Small keys are easily breakable. For DSA and RSA, keys should be at least
2048 bits long. For EC, keys should be at least 224 bits long.
## Example
```
from cryptography.hazmat.primitives.asymmetric import dsa, ec
dsa.generate_private_key(key_size=512)
ec.generate_private_key(curve=ec.SECT163K1())
```
## Use instead:
```
from cryptography.hazmat.primitives.asymmetric import dsa, ec
dsa.generate_private_key(key_size=4096)
ec.generate_private_key(curve=ec.SECP384R1())
```
# suspicious-non-cryptographic-random-usage (S311)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of cryptographically weak pseudo-random number generators.
## Why is this bad?
Cryptographically weak pseudo-random number generators are insecure, as they
are easily predictable. This can allow an attacker to guess the generated
numbers and compromise the security of the system.
Instead, use a cryptographically secure pseudo-random number generator
(such as using the secrets module)
when generating random numbers for security purposes.
In preview, this rule will also flag references to these generators.
## Example
```
import random
random.randrange(10)
```
## Use instead:
```
import secrets
secrets.randbelow(10)
```
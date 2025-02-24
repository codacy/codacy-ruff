# suspicious-pycrypto-import (S413)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of several unsafe cryptography modules.
## Why is this bad?
The pycrypto library is known to have a publicly disclosed buffer
overflow vulnerability. It is no longer actively maintained and has been
deprecated in favor of the pyca/cryptography library.
## Example
```
import Crypto.Random
```
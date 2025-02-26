# snmp-weak-cryptography (S509)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the SNMPv3 protocol without encryption.
## Why is this bad?
Unencrypted SNMPv3 communication can be intercepted and read by
unauthorized parties. Instead, enable encryption when using SNMPv3.
## Example
```
from pysnmp.hlapi import UsmUserData
UsmUserData("user")
```
## Use instead:
```
from pysnmp.hlapi import UsmUserData
UsmUserData("user", "authkey", "privkey")
```
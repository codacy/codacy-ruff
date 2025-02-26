# snmp-insecure-version (S508)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of SNMPv1 or SNMPv2.
## Why is this bad?
The SNMPv1 and SNMPv2 protocols are considered insecure as they do
not support encryption. Instead, prefer SNMPv3, which supports
encryption.
## Example
```
from pysnmp.hlapi import CommunityData
CommunityData("public", mpModel=0)
```
## Use instead:
```
from pysnmp.hlapi import CommunityData
CommunityData("public", mpModel=2)
```
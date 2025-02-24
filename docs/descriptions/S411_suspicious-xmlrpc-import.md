# suspicious-xmlrpc-import (S411)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the xmlrpc module.
## Why is this bad?
XMLRPC is a particularly dangerous XML module, as it is also concerned with
communicating data over a network. Use the defused.xmlrpc.monkey_patch()
function to monkey-patch the xmlrpclib module and mitigate remote XML
attacks.
## Example
```
import xmlrpc
```
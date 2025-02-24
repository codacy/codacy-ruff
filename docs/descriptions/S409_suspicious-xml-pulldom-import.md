# suspicious-xml-pulldom-import (S409)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the xml.dom.pulldom module.
## Why is this bad?
Using various methods from these modules to parse untrusted XML data is
known to be vulnerable to XML attacks. Replace vulnerable imports with the
equivalent defusedxml package, or make sure defusedxml.defuse_stdlib() is
called before parsing XML data.
## Example
```
import xml.dom.pulldom
```
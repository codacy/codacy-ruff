# suspicious-xml-etree-import (S405)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the xml.etree.cElementTree and xml.etree.ElementTree modules
## Why is this bad?
Using various methods from these modules to parse untrusted XML data is
known to be vulnerable to XML attacks. Replace vulnerable imports with the
equivalent defusedxml package, or make sure defusedxml.defuse_stdlib() is
called before parsing XML data.
## Example
```
import xml.etree.cElementTree
```
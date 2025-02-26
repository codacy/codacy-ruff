# suspicious-xml-element-tree-usage (S314)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of insecure XML parsers.
## Why is this bad?
Many XML parsers are vulnerable to XML attacks (such as entity expansion),
which cause excessive memory and CPU usage by exploiting recursion. An
attacker could use such methods to access unauthorized resources.
Consider using the defusedxml package when parsing untrusted XML data,
to protect against XML attacks.
In preview, this rule will also flag references to insecure XML parsers.
## Example
```
from xml.etree.ElementTree import parse
tree = parse("untrusted.xml")  # Vulnerable to XML attacks.
```
## Use instead:
```
from defusedxml.ElementTree import parse
tree = parse("untrusted.xml")
```
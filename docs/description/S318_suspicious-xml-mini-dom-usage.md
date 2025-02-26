# suspicious-xml-mini-dom-usage (S318)
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
from xml.dom.minidom import parse
content = parse("untrusted.xml")
```
## Use instead:
```
from defusedxml.minidom import parse
content = parse("untrusted.xml")
```
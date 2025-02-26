# suspicious-xmle-tree-usage (S320)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of insecure XML parsers.
## Why is this bad?
Many XML parsers are vulnerable to XML attacks (such as entity expansion),
which cause excessive memory and CPU usage by exploiting recursion. An
attacker could use such methods to access unauthorized resources.
In preview, this rule will also flag references to insecure XML parsers.
## Example
```
from lxml import etree
content = etree.parse("untrusted.xml")
```
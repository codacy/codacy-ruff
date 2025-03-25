# suspicious-xmle-tree-usage (S320)
Derived from the flake8-bandit linter.
Warning: This rule is deprecated and will be removed in a future release.
Deprecation
This rule was deprecated as the lxml library has been modified to address
known vulnerabilities and unsafe defaults. As such, the defusedxml
library is no longer necessary, defusedxml has deprecated its lxml
module.
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
# deprecated-c-element-tree (UP023)
Added in v0.0.199 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for uses of the xml.etree.cElementTree module.
## Why is this bad?
In Python 3.3, xml.etree.cElementTree was deprecated in favor of
xml.etree.ElementTree.
## Example
```
from xml.etree import cElementTree as ET
```
## Use instead:
```
from xml.etree import ElementTree as ET
```
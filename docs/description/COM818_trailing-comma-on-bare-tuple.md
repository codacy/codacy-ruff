# trailing-comma-on-bare-tuple (COM818)
Derived from the flake8-commas linter.
## What it does
Checks for the presence of trailing commas on bare (i.e., unparenthesized)
tuples.
## Why is this bad?
The presence of a misplaced comma will cause Python to interpret the value
as a tuple, which can lead to unexpected behaviour.
## Example
```
import json
foo = json.dumps({"bar": 1}),
```
## Use instead:
```
import json
foo = json.dumps({"bar": 1})
In the event that a tuple is intended, then use instead:
import json
foo = (json.dumps({"bar": 1}),)
```
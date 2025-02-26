# reimplemented-container-builtin (PIE807)
Derived from the flake8-pie linter.
Fix is sometimes available.
## What it does
Checks for lambdas that can be replaced with the list or dict builtins.
## Why is this bad?
Using container builtins are more succinct and idiomatic than wrapping
the literal in a lambda.
## Example
```
from dataclasses import dataclass, field
@dataclass
class Foo:
    bar: list[int] = field(default_factory=lambda: [])
```
## Use instead:
```
from dataclasses import dataclass, field
@dataclass
class Foo:
    bar: list[int] = field(default_factory=list)
    baz: dict[str, int] = field(default_factory=dict)
```
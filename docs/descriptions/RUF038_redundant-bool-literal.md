# redundant-bool-literal (RUF038)
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for Literal[True, False] type annotations.
## Why is this bad?
Literal[True, False] can be replaced with bool in type annotations,
which has the same semantic meaning but is more concise and readable.
bool type has exactly two constant instances: True and False. Static
type checkers such as mypy treat Literal[True, False] as equivalent to
bool in a type annotation.
## Example
```
from typing import Literal
x: Literal[True, False]
y: Literal[True, False, "hello", "world"]
```
## Use instead:
```
from typing import Literal
x: bool
y: Literal["hello", "world"] | bool
Fix safety
The fix for this rule is marked as unsafe, as it may change the semantics of the code.
Specifically:
Type checkers may not treat bool as equivalent when overloading boolean arguments
    with Literal[True] and Literal[False] (see, e.g., #14764 and #5421).
bool is not strictly equivalent to Literal[True, False], as bool is
    a subclass of int, and this rule may not apply if the type annotations are used
    in a numeric context.
Further, the Literal slice may contain trailing-line comments which the fix would remove.
```
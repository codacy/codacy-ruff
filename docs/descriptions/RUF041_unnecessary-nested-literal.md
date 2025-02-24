# unnecessary-nested-literal (RUF041)
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for unnecessary nested Literal.
## Why is this bad?
Prefer using a single Literal, which is equivalent and more concise.
Parameterization of literals by other literals is supported as an ergonomic
feature as proposed in [PEP 586], to enable patterns such as:
ReadOnlyMode         = Literal["r", "r+"]
WriteAndTruncateMode = Literal["w", "w+", "wt", "w+t"]
WriteNoTruncateMode  = Literal["r+", "r+t"]
AppendMode           = Literal["a", "a+", "at", "a+t"]
AllModes = Literal[ReadOnlyMode, WriteAndTruncateMode,
                  WriteNoTruncateMode, AppendMode]
As a consequence, type checkers also support nesting of literals
which is less readable than a flat Literal:
AllModes = Literal[Literal["r", "r+"], Literal["w", "w+", "wt", "w+t"],
                  Literal["r+", "r+t"], Literal["a", "a+", "at", "a+t"]]
## Example
```
AllModes = Literal[
    Literal["r", "r+"],
    Literal["w", "w+", "wt", "w+t"],
    Literal["r+", "r+t"],
    Literal["a", "a+", "at", "a+t"],
]
```
## Use instead:
```
AllModes = Literal[
    "r", "r+", "w", "w+", "wt", "w+t", "r+", "r+t", "a", "a+", "at", "a+t"
]
or assign the literal to a variable as in the first example.
Fix safety
The fix for this rule is marked as unsafe when the Literal slice is split
across multiple lines and some of the lines have trailing comments.
```
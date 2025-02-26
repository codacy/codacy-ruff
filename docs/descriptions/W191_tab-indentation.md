# tab-indentation (W191)
Derived from the pycodestyle linter.
## What it does
Checks for indentation that uses tabs.
## Why is this bad?
According to PEP 8, spaces are preferred over tabs (unless used to remain
consistent with code that is already indented with tabs).
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter enforces consistent indentation, making the rule redundant.
The rule is also incompatible with the formatter when using
format.indent-style="tab".
```
# ambiguous-unicode-character-docstring (RUF002)
Added in v0.0.102 ·
Related issues ·
View source
## What it does
Checks for ambiguous Unicode characters in docstrings.
## Why is this bad?
Some Unicode characters are visually similar to ASCII characters, but have
different code points. For example, GREEK CAPITAL LETTER ALPHA (U+0391)
is visually similar, but not identical, to the ASCII character A.
The use of ambiguous Unicode characters can confuse readers, cause subtle
bugs, and even make malicious code look harmless.
In preview, this rule will also flag Unicode characters that are
confusable with other, non-preferred Unicode characters. For example, the
spec recommends GREEK CAPITAL LETTER OMEGA over OHM SIGN.
You can omit characters from being flagged as ambiguous via the
lint.allowed-confusables setting.
## Example
```
"""A lovely docstring (with a `U+FF09` parenthesis）."""
```
## Use instead:
```
"""A lovely docstring (with no strange parentheses)."""
```
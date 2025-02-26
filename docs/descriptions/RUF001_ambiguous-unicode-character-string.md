# ambiguous-unicode-character-string (RUF001)
## What it does
Checks for ambiguous Unicode characters in strings.
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
print("Ηello, world!")  # "Η" is the Greek eta (`U+0397`).
```
## Use instead:
```
print("Hello, world!")  # "H" is the Latin capital H (`U+0048`).
```
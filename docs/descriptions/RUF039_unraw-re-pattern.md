# unraw-re-pattern (RUF039)
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Reports the following re and regex calls when
their first arguments are not raw strings:
For regex and re: compile, findall, finditer,
    fullmatch, match, search, split, sub, subn.
regex-specific: splititer, subf, subfn, template.
## Why is this bad?
Regular expressions should be written
using raw strings to avoid double escaping.
## Example
```
re.compile("foo\\bar")
```
## Use instead:
```
re.compile(r"foo\bar")
```
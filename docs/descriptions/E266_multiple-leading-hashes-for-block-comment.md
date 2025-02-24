# multiple-leading-hashes-for-block-comment (E266)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for block comments that start with multiple leading # characters.
## Why is this bad?
Per PEP 8, "Block comments generally consist of one or more paragraphs built
out of complete sentences, with each sentence ending in a period."
Each line of a block comment should start with a # followed by a single space.
Shebangs (lines starting with #!, at the top of a file) are exempt from this
rule.
## Example
```
### Block comment
```
## Use instead:
```
# Block comment
Alternatively, this rule makes an exception for comments that consist
solely of # characters, as in:
##############
# Block header
##############
```
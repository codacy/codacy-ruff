# indented-form-feed (RUF054)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for form feed characters preceded by either a space or a tab.
## Why is this bad?
The language reference states:
A formfeed character may be present at the start of the line;
it will be ignored for the indentation calculations above.
Formfeed characters occurring elsewhere in the leading whitespace
have an undefined effect (for instance, they may reset the space count to zero).
## Example
```
if foo():\n    \fbar()
```
## Use instead:
```
if foo():\n    bar()
```
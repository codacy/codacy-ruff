# unnecessary-regular-expression (RUF055)
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of the re module that can be replaced with builtin str methods.
## Why is this bad?
Performing checks on strings directly can make the code simpler, may require
less escaping, and will often be faster.
## Example
```
re.sub("abc", "", s)
```
## Use instead:
```
s.replace("abc", "")
Details
The rule reports the following calls when the first argument to the call is
a plain string literal, and no additional flags are passed:
re.sub
re.match
re.search
re.fullmatch
re.split
For re.sub, the repl (replacement) argument must also be a string literal,
not a function. For re.match, re.search, and re.fullmatch, the return
value must also be used only for its truth value.
Fix safety
This rule's fix is marked as unsafe if the affected expression contains comments. Otherwise,
the fix can be applied safely.
```
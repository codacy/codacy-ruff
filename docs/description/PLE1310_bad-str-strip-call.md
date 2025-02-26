# bad-str-strip-call (PLE1310)
Derived from the Pylint linter.
## What it does
Checks duplicate characters in str.strip calls.
## Why is this bad?
All characters in str.strip calls are removed from both the leading and
trailing ends of the string. Including duplicate characters in the call
is redundant and often indicative of a mistake.
In Python 3.9 and later, you can use str.removeprefix and
str.removesuffix to remove an exact prefix or suffix from a string,
respectively, which should be preferred when possible.
## Example
```
# Evaluates to "foo".
"bar foo baz".strip("bar baz ")
```
## Use instead:
```
# Evaluates to "foo".
"bar foo baz".strip("abrz ")  # "foo"
Or:
# Evaluates to "foo".
"bar foo baz".removeprefix("bar ").removesuffix(" baz")
```
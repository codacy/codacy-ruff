# ambiguous-variable-name (E741)
Derived from the pycodestyle linter.
## What it does
Checks for the use of the characters 'l', 'O', or 'I' as variable names.
Note: This rule is automatically disabled for all stub files
(files with .pyi extensions). The rule has little relevance for authors
of stubs: a well-written stub should aim to faithfully represent the
interface of the equivalent .py file as it exists at runtime, including any
ambiguously named variables in the runtime module.
## Why is this bad?
In some fonts, these characters are indistinguishable from the
numerals one and zero. When tempted to use 'l', use 'L' instead.
## Example
```
l = 0
O = 123
I = 42
```
## Use instead:
```
L = 0
o = 123
i = 42
```
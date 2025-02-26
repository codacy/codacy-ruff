# format-literals (UP030)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for unnecessary positional indices in format strings.
## Why is this bad?
In Python 3.1 and later, format strings can use implicit positional
references. For example, "{0}, {1}".format("Hello", "World") can be
rewritten as "{}, {}".format("Hello", "World").
If the positional indices appear exactly in-order, they can be omitted
in favor of automatic indices to improve readability.
## Example
```
"{0}, {1}".format("Hello", "World")  # "Hello, World"
```
## Use instead:
```
"{}, {}".format("Hello", "World")  # "Hello, World"
```
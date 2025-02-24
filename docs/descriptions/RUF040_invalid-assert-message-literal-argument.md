# invalid-assert-message-literal-argument (RUF040)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for invalid use of literals in assert message argument.
## Why is this bad?
An assert message which is a non-string literal was likely intended
to be used in a comparison assertion, rather than as a message.
## Example
```
fruits = ["apples", "plums", "pears"]
fruits.filter(lambda fruit: fruit.startwith("p"))
assert len(fruits), 2  # True unless the list is empty
```
## Use instead:
```
fruits = ["apples", "plums", "pears"]
fruits.filter(lambda fruit: fruit.startwith("p"))
assert len(fruits) == 2
```
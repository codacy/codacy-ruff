# multiple-starts-ends-with (PIE810)
Derived from the flake8-pie linter.
Fix is always available.
## What it does
Checks for startswith or endswith calls on the same value with
different prefixes or suffixes.
## Why is this bad?
The startswith and endswith methods accept tuples of prefixes or
suffixes respectively. Passing a tuple of prefixes or suffixes is more
efficient and readable than calling the method multiple times.
## Example
```
msg = "Hello, world!"
if msg.startswith("Hello") or msg.startswith("Hi"):
    print("Greetings!")
```
## Use instead:
```
msg = "Hello, world!"
if msg.startswith(("Hello", "Hi")):
    print("Greetings!")
Fix safety
This rule's fix is unsafe, as in some cases, it will be unable to determine
whether the argument to an existing .startswith or .endswith call is a
tuple. For example, given msg.startswith(x) or msg.startswith(y), if x
or y is a tuple, and the semantic model is unable to detect it as such,
the rule will suggest msg.startswith((x, y)), which will error at
runtime.
```
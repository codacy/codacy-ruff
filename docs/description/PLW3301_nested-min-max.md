# nested-min-max (PLW3301)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for nested min and max calls.
## Why is this bad?
Nested min and max calls can be flattened into a single call to improve
readability.
## Example
```
minimum = min(1, 2, min(3, 4, 5))
maximum = max(1, 2, max(3, 4, 5))
diff = maximum - minimum
```
## Use instead:
```
minimum = min(1, 2, 3, 4, 5)
maximum = max(1, 2, 3, 4, 5)
diff = maximum - minimum
```
# invalid-formatter-suppression-comment (RUF028)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for formatter suppression comments that are ineffective or incompatible
with Ruff's formatter.
## Why is this bad?
Suppression comments that do not actually prevent formatting could cause unintended changes
when the formatter is run.
## Examples
```
In the following example, all suppression comments would cause
a rule violation.
def decorator():
    pass
@decorator
# fmt: off
def example():
    if True:
        # fmt: skip
        expression = [
            # fmt: off
            1,
            2,
        ]
        # yapf: disable
    # fmt: on
    # yapf: enable
```
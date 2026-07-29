# unused-noqa (RUF100)
Added in v0.0.155 ·
Related issues ·
View source
Fix is always available.
## What it does
Checks for noqa directives that are no longer applicable.
## Why is this bad?
A noqa directive that no longer matches any diagnostic violations is
likely included by mistake, and should be removed to avoid confusion.
## Example
```
import foo  # noqa: F401
def bar():
    foo.bar()
```
## Use instead:
```
import foo
def bar():
    foo.bar()
Conflict with other linters
When using RUF100 with the --fix option, Ruff may remove trailing comments
that follow a # noqa directive on the same line, as it interprets the
remainder of the line as a description for the suppression.
To prevent Ruff from removing suppressions for other tools (like pylint
or mypy), separate them with a second # character:
# Bad: Ruff --fix will remove the pylint comment
def visit_ImportFrom(self, node):  # noqa: N802, pylint: disable=invalid-name
    pass
# Good: Ruff will preserve the pylint comment
def visit_ImportFrom(self, node):  # noqa: N802 # pylint: disable=invalid-name
    pass
Fix safety
The rule's fix is marked as unsafe when a full suppression comment would be removed and there
are other nested comments on the same line. Removing such a comment can change the behavior of
other suppression comments before or after the removed comment.
See also
This rule ignores any codes that are unknown to Ruff, as it can't determine
if the codes are valid or used by other tools. Enable invalid-rule-code
to flag any unknown rule codes.
```
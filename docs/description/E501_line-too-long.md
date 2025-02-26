# line-too-long (E501)
Derived from the pycodestyle linter.
## What it does
Checks for lines that exceed the specified maximum character length.
## Why is this bad?
Overlong lines can hurt readability. PEP 8, for example, recommends
limiting lines to 79 characters. By default, this rule enforces a limit
of 88 characters for compatibility with Black and the Ruff formatter,
though that limit is configurable via the line-length setting.
In the interest of pragmatism, this rule makes a few exceptions when
determining whether a line is overlong. Namely, it:
Ignores lines that consist of a single "word" (i.e., without any
    whitespace between its characters).
Ignores lines that end with a URL, as long as the URL starts before
    the line-length threshold.
Ignores line that end with a pragma comment (e.g., # type: ignore
    or # noqa), as long as the pragma comment starts before the
    line-length threshold. That is, a line will not be flagged as
    overlong if a pragma comment causes it to exceed the line length.
    (This behavior aligns with that of the Ruff formatter.)
Ignores SPDX license identifiers and copyright notices
    (e.g., # SPDX-License-Identifier: MIT), which are machine-readable
    and should not wrap over multiple lines.
If lint.pycodestyle.ignore-overlong-task-comments is true, this rule will
also ignore comments that start with any of the specified lint.task-tags
(e.g., # TODO:).
## Example
```
my_function(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10)
```
## Use instead:
```
my_function(
    param1, param2, param3, param4, param5,
    param6, param7, param8, param9, param10
)
Error suppression
Hint: when suppressing E501 errors within multi-line strings (like
docstrings), the noqa directive should come at the end of the string
(after the closing triple quote), and will apply to the entire string, like
so:
"""Lorem ipsum dolor sit amet.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
"""  # noqa: E501
```
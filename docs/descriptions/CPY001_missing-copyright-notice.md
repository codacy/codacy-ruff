# missing-copyright-notice (CPY001)
Derived from the flake8-copyright linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for the absence of copyright notices within Python files.
Note that this check only searches within the first 4096 bytes of the file.
## Why is this bad?
In some codebases, it's common to have a license header at the top of every
file. This rule ensures that the license header is present.
```
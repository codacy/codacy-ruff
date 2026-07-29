# missing-copyright-notice (CPY001)
Added in 0.16.0 ·
Related issues ·
View source
Derived from the flake8-copyright linter.
## What it does
Checks for the absence of copyright notices within Python files.
Note that this check only searches within the first 4096 bytes of the file.
## Why is this bad?
In some codebases, it's common to have a license header at the top of every
file. This rule ensures that the license header is present.
```
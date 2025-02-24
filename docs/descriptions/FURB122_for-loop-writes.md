# for-loop-writes (FURB122)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for the use of IOBase.write in a for loop.
## Why is this bad?
When writing a batch of elements, it's more idiomatic to use a single method call to
IOBase.writelines, rather than write elements one by one.
## Example
```
with Path("file").open("w") as f:
    for line in lines:
        f.write(line)
with Path("file").open("wb") as f:
    for line in lines:
        f.write(line.encode())
```
## Use instead:
```
with Path("file").open("w") as f:
    f.writelines(lines)
with Path("file").open("wb") as f:
    f.writelines(line.encode() for line in lines)
```
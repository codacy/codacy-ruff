# invalid-pyproject-toml (RUF200)
## What it does
Checks for any pyproject.toml that does not conform to the schema from the relevant PEPs.
## Why is this bad?
Your project may contain invalid metadata or configuration without you noticing
## Example
```
[project]
name = "crab"
version = "1.0.0"
authors = ["Ferris the Crab <[email protected]>"]
```
## Use instead:
```
[project]
name = "crab"
version = "1.0.0"
authors = [
  { name = "Ferris the Crab", email = "[email protected]" }
]
```
# unsafe-yaml-load (S506)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the yaml.load function.
## Why is this bad?
Running the yaml.load function over untrusted YAML files is insecure, as
yaml.load allows for the creation of arbitrary Python objects, which can
then be used to execute arbitrary code.
Instead, consider using yaml.safe_load, which allows for the creation of
simple Python objects like integers and lists, but prohibits the creation of
more complex objects like functions and classes.
## Example
```
import yaml
yaml.load(untrusted_yaml)
```
## Use instead:
```
import yaml
yaml.safe_load(untrusted_yaml)
```
# suspicious-marshal-usage (S302)
Derived from the flake8-bandit linter.
## What it does
Checks for calls to marshal functions.
## Why is this bad?
Deserializing untrusted data with marshal is insecure, as it can allow for
the creation of arbitrary objects, which can then be used to achieve
arbitrary code execution and otherwise unexpected behavior.
Avoid deserializing untrusted data with marshal. Instead, consider safer
formats, such as JSON.
If you must deserialize untrusted data with marshal, consider signing the
data with a secret key and verifying the signature before deserializing the
payload. This will prevent an attacker from injecting arbitrary objects
into the serialized data.
In preview, this rule will also flag references to marshal functions.
## Example
```
import marshal
with open("foo.marshal", "rb") as file:
    foo = marshal.load(file)
```
## Use instead:
```
import json
with open("foo.json", "rb") as file:
    foo = json.load(file)
```
# suspicious-pickle-usage (S301)
Derived from the flake8-bandit linter.
## What it does
Checks for calls to pickle functions or modules that wrap them.
## Why is this bad?
Deserializing untrusted data with pickle and other deserialization
modules is insecure as it can allow for the creation of arbitrary objects,
which can then be used to achieve arbitrary code execution and otherwise
unexpected behavior.
Avoid deserializing untrusted data with pickle and other deserialization
modules. Instead, consider safer formats, such as JSON.
If you must deserialize untrusted data with pickle, consider signing the
data with a secret key and verifying the signature before deserializing the
payload, This will prevent an attacker from injecting arbitrary objects
into the serialized data.
In preview, this rule will also flag references to pickle functions.
## Example
```
import pickle
with open("foo.pickle", "rb") as file:
    foo = pickle.load(file)
```
## Use instead:
```
import json
with open("foo.json", "rb") as file:
    foo = json.load(file)
```
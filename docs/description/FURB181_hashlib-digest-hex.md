# hashlib-digest-hex (FURB181)
Derived from the refurb linter.
Fix is sometimes available.
## What it does
Checks for the use of .digest().hex() on a hashlib hash, like sha512.
## Why is this bad?
When generating a hex digest from a hash, it's preferable to use the
.hexdigest() method, rather than calling .digest() and then .hex(),
as the former is more concise and readable.
## Example
```
from hashlib import sha512
hashed = sha512(b"some data").digest().hex()
```
## Use instead:
```
from hashlib import sha512
hashed = sha512(b"some data").hexdigest()
```
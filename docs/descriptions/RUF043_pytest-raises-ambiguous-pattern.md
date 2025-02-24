# pytest-raises-ambiguous-pattern (RUF043)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for non-raw literal string arguments passed to the match parameter
of pytest.raises() where the string contains at least one unescaped
regex metacharacter.
## Why is this bad?
The match argument is implicitly converted to a regex under the hood.
It should be made explicit whether the string is meant to be a regex or a "plain" pattern
by prefixing the string with the r suffix, escaping the metacharacter(s)
in the string using backslashes, or wrapping the entire string in a call to
re.escape().
## Example
```
import pytest
with pytest.raises(Exception, match="A full sentence."):
    do_thing_that_raises()
```
## Use instead:
```
import pytest
with pytest.raises(Exception, match=r"A full sentence."):
    do_thing_that_raises()
Alternatively:
import pytest
import re
with pytest.raises(Exception, match=re.escape("A full sentence.")):
    do_thing_that_raises()
or:
import pytest
import re
with pytest.raises(Exception, "A full sentence\\."):
    do_thing_that_raises()
```
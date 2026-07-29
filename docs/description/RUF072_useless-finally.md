# useless-finally (RUF072)
Preview (since 0.15.8) ·
Related issues ·
View source
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for finally clauses that only contain pass or ... statements
## Why is this bad?
An empty finally clause is a no-op and adds unnecessary noise.
If the try statement has except or else clauses, the finally
clause can simply be removed. If it's a bare try/finally, the entire
try statement can be replaced with its body
## Example
```
try:
    foo()
except Exception:
    bar()
finally:
    pass
```
## Use instead:
```
try:
    foo()
except Exception:
    bar()
## Example
```
try:
    foo()
finally:
    pass
```
## Use instead:
```
foo()
See also
[needless-else][RUF047]: Removes empty else clauses on try (and
    other statements). Both rules can fire on the same try statement
[suppressible-exception][SIM105]: Rewrites try/except: pass to
    contextlib.suppress(). Won't apply while a finally clause is present,
    so RUF072 must remove it first
[useless-try-except][TRY203]: Flags try/except that only re-raises
```
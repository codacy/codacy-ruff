# bare-except (E722)
Derived from the pycodestyle linter.
## What it does
Checks for bare except catches in try-except statements.
## Why is this bad?
A bare except catches BaseException which includes
KeyboardInterrupt, SystemExit, Exception, and others. Catching
BaseException can make it hard to interrupt the program (e.g., with
Ctrl-C) and can disguise other problems.
## Example
```
try:
    raise KeyboardInterrupt("You probably don't mean to break CTRL-C.")
except:
    print("But a bare `except` will ignore keyboard interrupts.")
```
## Use instead:
```
try:
    do_something_that_might_break()
except MoreSpecificException as e:
    handle_error(e)
If you actually need to catch an unknown error, use Exception which will
catch regular program errors but not important system exceptions.
def run_a_function(some_other_fn):
    try:
        some_other_fn()
    except Exception as e:
        print(f"How exceptional! {e}")
```
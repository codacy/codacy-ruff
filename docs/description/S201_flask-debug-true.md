# flask-debug-true (S201)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of debug=True in Flask.
## Why is this bad?
Enabling debug mode shows an interactive debugger in the browser if an
error occurs, and allows running arbitrary Python code from the browser.
This could leak sensitive information, or allow an attacker to run
arbitrary code.
## Example
```
import flask
app = Flask()
app.run(debug=True)
```
## Use instead:
```
import flask
app = Flask()
app.run(debug=os.environ["ENV"] == "dev")
```
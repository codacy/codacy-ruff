# hardcoded-sql-expression (S608)
Derived from the flake8-bandit linter.
## What it does
Checks for strings that resemble SQL statements involved in some form
string building operation.
## Why is this bad?
SQL injection is a common attack vector for web applications. Directly
interpolating user input into SQL statements should always be avoided.
Instead, favor parameterized queries, in which the SQL statement is
provided separately from its parameters, as supported by psycopg3
and other database drivers and ORMs.
## Example
```
query = "DELETE FROM foo WHERE id = '%s'" % identifier
```
# ssh-no-host-key-verification (S507)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of policies disabling SSH verification in Paramiko.
## Why is this bad?
By default, Paramiko checks the identity of the remote host when establishing
an SSH connection. Disabling the verification might lead to the client
connecting to a malicious host, without the client knowing.
## Example
```
from paramiko import client
ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
```
## Use instead:
```
from paramiko import client
ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.RejectPolicy)
```
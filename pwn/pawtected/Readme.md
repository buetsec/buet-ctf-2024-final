# Pawtected

## Description

My cat is my guardian angle. She will protect my sea shells.

[pawtected](./pawtected.zip)

> `nc 178.128.214.190 1337`

> *Note:* Create a `flag.txt` file in the same folder as the Dockerfile for local debugging.

## Solution

This challenge involves leaking the canary and a stack address and then returning to libc to get shell.
You can either use onegadgets or any other method to come up with your ret2libc.

[solution](./solve.py)

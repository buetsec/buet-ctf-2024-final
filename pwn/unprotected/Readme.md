# Unprotected

## Description

Some customers complained they needed to disable protection to run the programs.
So, we had to comply... What could possibly go wrong?


[unprotected](./unprotected.zip)

> `nc 178.128.214.190 1348`

> *Note:* Create a `flag.txt` file in the same folder as the Dockerfile for local debugging.

## Solution

This challenge involves overflowing the buffer to return to win function to get shell.

[solution](./solve.py)

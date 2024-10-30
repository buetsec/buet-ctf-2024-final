# Meowlibc

## Description

My cat was supposed to keep you safe. But it could not because you were given it's meowlibc.
Now, no meowlibc for you. And also, no container for you.

[chal](./chal)

> `nc 178.128.214.190 1740`

## Solution

This challenge involves leaking the canary and a stack address but without knowing the libc and then returning to main and again leak system
and then returning to system to get shell. As we do not have access to the libc, we cannot guess where the system will be but we can leak it
from it's got entry also, we have the /bin/sh string in our binary. we can pass this to system as our argument.

[solution](./solve.py)

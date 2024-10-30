FROM ubuntu AS app

FROM pwn.red/jail
COPY --from=app / /srv

COPY flag.txt /srv/app/
COPY ld-linux-x86-64.so.2 /srv/app/
COPY glibc /srv/app/glibc/
COPY chal /srv/app/run

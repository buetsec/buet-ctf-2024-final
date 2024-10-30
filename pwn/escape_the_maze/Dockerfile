FROM python:slim AS app
RUN pip install --no-cache-dir progress

FROM pwn.red/jail
COPY --from=app / /srv
COPY Escape_The_Maze.py /srv/app/chal.py
RUN sed -i 's/\r$//' /srv/app/chal.py
COPY run.sh /srv/app/run

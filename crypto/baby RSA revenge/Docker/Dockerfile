FROM python:slim AS app
RUN pip install --no-cache-dir progress 
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM pwn.red/jail
COPY --from=app / /srv
COPY flag.txt /srv/app/flag.txt
COPY server.py /srv/app/chal.py
RUN sed -i 's/\r$//' /srv/app/chal.py
COPY run.sh /srv/app/run

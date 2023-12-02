FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential ffmpeg\
    && pip install --no-cache-dir --upgrade pip

ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

WORKDIR /app
COPY ./requirements.txt /app/

RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app/

CMD ["python3", "consumer.py"]
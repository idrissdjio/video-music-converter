FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev mariadb-client \
    && pip install --no-cache-dir --upgrade pip

ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

WORKDIR /app
COPY ./requirements.txt /app/

# Uninstall the jwt package if it exists
RUN pip uninstall -y jwt || true

# Install requirements (now without jwt, assuming it's removed from requirements.txt)
RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python3", "server.py"]
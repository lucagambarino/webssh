FROM python:3.13-alpine3.21

LABEL maintainer='Luca Gambarino'
LABEL version='3.13-alpine3.21'

ADD . /code
WORKDIR /code

RUN \
  apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    cargo \
    make && \
  pip install --no-cache-dir -r requirements.txt && \
  apk del .build-deps && \
  addgroup -S webssh && \
  adduser -S -s /bin/false -G webssh webssh && \
  chown -R webssh:webssh /code

EXPOSE 8888/tcp
USER webssh
CMD ["python", "run.py"]

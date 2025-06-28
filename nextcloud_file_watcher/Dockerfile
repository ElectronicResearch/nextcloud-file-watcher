ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip

COPY rootfs /  # wichtig: rootfs muss korrekt kopiert werden!
COPY briefkasten_watcher.py /briefkasten_watcher.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

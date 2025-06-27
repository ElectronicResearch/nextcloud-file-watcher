ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip

COPY run.sh /run.sh
COPY briefkasten_watcher.py /briefkasten_watcher.py
COPY rootfs/etc/services.d/app/run /etc/services.d/app/run

RUN chmod +x /run.sh
RUN chmod +x /etc/services.d/app/run
CMD [ "/run.sh" ]

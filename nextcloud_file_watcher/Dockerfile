ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip curl
COPY run.sh /run.sh
RUN chmod +x /run.sh

COPY nextcloud_file_watcher /

RUN pip3 install requests

CMD [ "/run.sh" ]

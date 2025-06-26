ARG BUILD_FROM=ghcr.io/home-assistant/amd64-addon-python:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

# Falls Python-Pakete benötigt werden:
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

# Dein Skript kopieren
COPY run.sh /run.sh
RUN chmod +x /run.sh

# s6 benötigt diese Startstruktur
COPY rootfs/ /

# Startpunkt (nicht direkt /run.sh!)
CMD [ "/init" ]

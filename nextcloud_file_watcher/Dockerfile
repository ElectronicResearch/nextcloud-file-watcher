ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

# Installiere Python und pip
RUN apk add --no-cache python3 py3-pip py3-requests

# Skripte und Konfiguration kopieren
COPY rootfs / # <- wichtig: enthält /etc/services.d/app/run
COPY briefkasten_watcher.py /app/briefkasten_watcher.py

# Muss vorhanden sein – startet das S6-Overlay-System
CMD ["/init"]

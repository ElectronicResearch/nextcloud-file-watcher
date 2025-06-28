ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

# Python und Pip installieren
RUN apk add --no-cache python3 py3-pip

# Optional: Abhängigkeiten (z. B. für nextcloud-API etc.)
# Beispiel: RUN pip3 install requests nextcloud-client

# Skript kopieren
COPY briefkasten_watcher.py /app/briefkasten_watcher.py

# Startskripte für s6-overlay
COPY rootfs /

# ❗ wichtig: S6 startet über /init (PID 1)
CMD ["/init"]

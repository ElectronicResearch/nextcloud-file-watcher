FROM python:3.11-slim

# System-Abhängigkeiten installieren (z. B. für requests + evtl. XML)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis setzen
WORKDIR /app

# Skript + Konfig kopieren
COPY briefkasten_watcher.py /app/
COPY config.json /app/

# Python-Abhängigkeiten installieren
RUN pip install --no-cache-dir requests

# Ausführbares Skript starten
CMD ["python", "/app/briefkasten_watcher.py"]

#!/usr/bin/with-contenv bashio

export SUPERVISOR_TOKEN=$SUPERVISOR_TOKEN

echo "[INFO] Starte Nextcloud Watcher..."
python3 /briefkasten_watcher.py


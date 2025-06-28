import os
import time
# import requests
import json
import logging
# ==== Lade Konfiguration ====
NEXTCLOUD_URL = os.getenv("NEXTCLOUD_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
WATCH_FOLDER = os.getenv("WATCH_FOLDER", "Briefkasten")
FILE_TYPES_RAW = os.getenv("FILE_TYPES", "")
INTERVAL = int(os.getenv("INTERVAL", "600"))
NOTIFY_SERVICE = os.getenv("NOTIFY_SERVICE")
ENABLE_CONTACT_LOOKUP = os.getenv("ENABLE_CONTACT_LOOKUP", "false").lower() == "true"

# Dateitypen als Liste
FILE_TYPES = [ext.strip().lower() for ext in FILE_TYPES_RAW.split(",") if ext.strip()]

# URL zur Nextcloud-API (WebDAV)
WEBDAV_URL = f"{NEXTCLOUD_URL}/remote.php/dav/files/{USERNAME}/{WATCH_FOLDER}/"

# Für einfache Duplikatserkennung
known_files = set()


def send_notification(message):
    """Sendet eine Benachrichtigung an Home Assistant über die REST API."""
    if not NOTIFY_SERVICE:
        print("Kein Benachrichtigungsdienst angegeben.")
        return

    payload = {
        "message": message,
        "title": "📬 Neuer Upload in Nextcloud"
    }

    try:
        response = requests.post(
            f"http://supervisor/core/api/services/{NOTIFY_SERVICE.replace('.', '/')}",
            headers={
                "Authorization": f"Bearer {os.getenv('SUPERVISOR_TOKEN')}",
                "Content-Type": "application/json"
            },
            data=json.dumps(payload)
        )
        if response.status_code != 200:
            print("Fehler beim Senden der Benachrichtigung:", response.text)
    except Exception as e:
        print("Exception bei Benachrichtigung:", e)


def list_files():
    """Listet alle Dateien im Zielordner via WebDAV."""
    try:
        response = requests.request("PROPFIND", WEBDAV_URL, auth=(USERNAME, PASSWORD), headers={
            "Depth": "1"
        })
        if response.status_code >= 300:
            print("Fehler beim Abrufen von Dateien:", response.status_code)
            return []

        # Primitive Dateinamenerkennung aus dem XML-Antworttext
        files = []
        for line in response.text.splitlines():
            if "<d:href>" in line:
                start = line.find("<d:href>") + 8
                end = line.find("</d:href>")
                path = line[start:end]
                filename = os.path.basename(path)
                if any(filename.lower().endswith(ext) for ext in FILE_TYPES):
                    files.append(filename)

        return files
    except Exception as e:
        print("Fehler beim Listen von Dateien:", e)
        return []


def main_loop():
    print("📂 Nextcloud File Watcher gestartet.")
    while True:
        try:
            current_files = list_files()

            new_files = [f for f in current_files if f not in known_files]
            if new_files:
                for f in new_files:
                    send_notification(f"Neue Datei: {f}")
                    print("📥 Neue Datei erkannt:", f)
                known_files.update(new_files)

        except Exception as e:
            print("Fehler in main loop:", e)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main_loop()

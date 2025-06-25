# Nextcloud File Watcher Add-on

Dieses Home Assistant Add-on überwacht einen Nextcloud-Ordner und sendet Benachrichtigungen bei neuen Dateien.

## Konfiguration

- `nextcloud_url`: URL deiner Nextcloud-Instanz
- `username` / `password`: Zugangsdaten
- `watch_folder`: Ordnername (z. B. "Briefkasten")
- `interval`: Zeitintervall in Sekunden
- `file_types`: Erlaubte Dateiendungen (z. B. `.jpg`, `.pdf`)
- `notify_service`: z. B. `notify.mobile_app_...`
- `enable_contact_lookup`: true/false

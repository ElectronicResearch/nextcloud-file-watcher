# 📬 Nextcloud File Watcher

Ein Home Assistant Add-on, das Nextcloud-Ordner überwacht und bei neuen Dateien Push-Benachrichtigungen sendet.

## 🚀 Features

- 🔄 Automatische Überwachung von Nextcloud-Ordnern
- 🔔 Push-Benachrichtigungen über Home Assistant Mobile App
- 🎯 Filterung nach Dateiendungen (z.B. nur `.jpg`, `.pdf`)
- 👤 Optionale Kontakt-Suche basierend auf Dateinamen
- ⚙️ Vollständig konfigurierbar über Home Assistant UI
- 📝 Detailliertes Logging

## ⚙️ Konfiguration

| Option | Beschreibung | Beispiel |
|--------|-------------|----------|
| `nextcloud_url` | Nextcloud Server URL | `https://cloud.example.com` |
| `username` | Nextcloud Benutzername | `max.mustermann` |
| `password` | Nextcloud Passwort | `geheim123` |
| `watch_folder` | Zu überwachender Ordner | `Briefkasten` |
| `interval` | Prüfintervall in Sekunden | `600` (10 Minuten) |
| `file_types` | Erlaubte Dateiendungen | `["jpg", "pdf"]` |
| `notify_service` | Benachrichtigungsservice | `notify.mobile_app_mein_telefon` |
| `enable_contact_lookup` | Kontakt-Suche aktivieren | `true` |

## 📱 Home Assistant Benachrichtigungen

Das Add-on verwendet den internen Supervisor-Zugriff auf den Home Assistant Core und sendet Benachrichtigungen an dein konfiguriertes Mobile Device über den Dienst `notify.mobile_app_dein_gerät`.

Stelle sicher, dass du die richtige `notify`-Service-Entität verwendest (z.B. `mobile_app_iphone_von_max`).

## 🔒 Sicherheit

Deine Zugangsdaten werden **nicht** gespeichert oder übertragen. Sie verbleiben in der Home Assistant-Konfiguration und werden beim Start des Add-ons übergeben.

## 📋 Installation

1. **Add-on-Repository hinzufügen**  
   Gehe in Home Assistant zu:  
   `Einstellungen → Add-ons → Add-on Store → ⋯ → Repository hinzufügen`  
   Füge dort folgendes GitHub-Repo hinzu:  
   `https://github.com/ElectronicResearch/nextcloud-file-watcher`

2. **Add-on installieren**
   - Suche nach "Nextcloud File Watcher"
   - Klicke auf "Installieren"
   - Konfiguriere die Einstellungen
   - Starte das Add-on

## 🔧 Verwendung

Das Add-on ist ideal für:
- Digitale Briefkästen
- Gemeinsame Cloud-Ordner
- Automatische Benachrichtigungen bei neuen Dokumenten
- Überwachung von Upload-Ordnern

## 📝 Logs

Das Add-on bietet detailliertes Logging. Du findest die Logs unter:
- Add-on → Logs
- Entwicklertools → Logs (wenn verfügbar)

## 🐛 Fehlerbehebung

### Add-on startet nicht
- Prüfe die Konfiguration
- Stelle sicher, dass alle Pflichtfelder ausgefüllt sind
- Prüfe die Logs auf Fehlermeldungen

### Keine Benachrichtigungen
- Prüfe den `notify_service` Namen
- Stelle sicher, dass die Mobile App installiert ist
- Teste den Benachrichtigungsservice manuell

### Verbindungsfehler
- Prüfe die Nextcloud URL
- Stelle sicher, dass die Zugangsdaten korrekt sind
- Prüfe die Netzwerkverbindung

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz.

---

**Entwickelt von Electronic Research** 
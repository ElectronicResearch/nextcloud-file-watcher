#!/usr/bin/env python3
"""
Nextcloud Briefkasten Watcher - Home Assistant Add-on
Überwacht Nextcloud-Ordner und sendet Push-Benachrichtigungen
"""

import os
import time
import requests
from xml.etree import ElementTree as ET
import json
import logging

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    """Lädt die Konfiguration aus der options.json"""
    try:
        with open('/data/options.json') as f:
            config = json.load(f)
            logger.info("Konfiguration erfolgreich geladen")
            return config
    except Exception as e:
        logger.error(f"Fehler beim Laden der Konfiguration: {e}")
        return None

def list_remote_files(config):
    """Listet alle Dateien im überwachten Nextcloud-Ordner"""
    try:
        url = f"{config['nextcloud_url']}/remote.php/dav/files/{config['username']}/{config['watch_folder']}/"
        response = requests.request(
            method="PROPFIND",
            url=url,
            auth=(config['username'], config['password']),
            headers={"Depth": "1"},
            timeout=30
        )
        
        if response.status_code != 207:
            logger.error(f"Fehler bei der WebDAV-Abfrage: {response.status_code}")
            return []

        xml = ET.fromstring(response.content)
        ns = {'d': 'DAV:'}
        files = []
        
        for response_elem in xml.findall('d:response', ns):
            href = response_elem.find('d:href', ns).text
            filename = href.split('/')[-1]
            if filename and not filename.endswith('/'):
                files.append(filename)
        
        logger.info(f"{len(files)} Dateien im Ordner gefunden")
        return files
        
    except Exception as e:
        logger.error(f"Fehler beim Abrufen der Dateien: {e}")
        return []

def lookup_contact_owner(filename, config):
    """Sucht nach Kontakten basierend auf dem Dateinamen"""
    if not config.get("enable_contact_lookup"):
        return None
        
    try:
        user_hint = filename.split('_')[0]
        response = requests.get(
            f"{config['nextcloud_url']}/index.php/apps/contacts/api/v1/contact",
            auth=(config['username'], config['password']),
            timeout=10
        )
        
        if response.status_code == 200:
            contacts = response.json()
            for contact in contacts:
                if user_hint.lower() in json.dumps(contact).lower():
                    return contact.get('FN') or contact.get('name')
                    
    except Exception as e:
        logger.warning(f"Kontakt-Suche fehlgeschlagen: {e}")
    
    return None

def send_notification(config, filename, sender=None):
    """Sendet eine Benachrichtigung über Home Assistant"""
    try:
        message = f"📬 Neue Datei: {filename}"
        if sender:
            message += f" (von {sender})"
            
        payload = {
            "message": message,
            "title": "Neuer Einwurf im Briefkasten"
        }
        
        url = f"http://supervisor/core/api/services/{config['notify_service'].replace('.', '/')}"
        headers = {
            "Authorization": f"Bearer {os.getenv('SUPERVISOR_TOKEN')}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            logger.info(f"✅ Benachrichtigung gesendet: {filename}")
        else:
            logger.error(f"❌ Fehler bei Benachrichtigung: {response.status_code}")
            
    except Exception as e:
        logger.error(f"❌ Fehler beim Senden der Benachrichtigung: {e}")

def main():
    """Hauptfunktion"""
    logger.info("🚀 Nextcloud Briefkasten Watcher gestartet")
    
    config = load_config()
    if not config:
        logger.error("Konfiguration konnte nicht geladen werden. Beende Add-on.")
        return
    
    logger.info(f"📁 Überwache Ordner: {config.get('watch_folder', 'Nicht konfiguriert')}")
    logger.info(f"⏰ Intervall: {config.get('interval', 600)} Sekunden")
    logger.info(f"📄 Dateitypen: {config.get('file_types', [])}")
    logger.info("-" * 50)
    
    seen_files = set()

    while True:
        try:
            current_files = list_remote_files(config)
            if current_files is None:
                logger.warning("Konnte Dateien nicht abrufen, warte auf nächsten Zyklus")
                time.sleep(config.get('interval', 600))
                continue
                
            new_files = [
                f for f in current_files 
                if f not in seen_files and 
                any(f.lower().endswith(ext.lower()) for ext in config.get('file_types', []))
            ]
            
            for file in new_files:
                logger.info(f"📬 Neue Datei gefunden: {file}")
                sender = lookup_contact_owner(file, config)
                send_notification(config, file, sender)
            
            seen_files.update(new_files)
            logger.info(f"✅ Überwachung abgeschlossen. {len(current_files)} Dateien gefunden.")
            
        except Exception as e:
            logger.error(f"❌ Unerwarteter Fehler: {e}")
        
        sleep_time = config.get('interval', 600)
        logger.info(f"⏳ Warte {sleep_time} Sekunden...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main() 
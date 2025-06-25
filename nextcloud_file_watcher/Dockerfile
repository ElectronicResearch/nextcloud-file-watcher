FROM python:3.11-slim

WORKDIR /app

COPY nextcloud_file_watcher/briefkasten_watcher.py /app/
COPY config.json /app/

RUN pip install requests

CMD ["python", "/app/briefkasten_watcher.py"]


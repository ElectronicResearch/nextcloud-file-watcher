 #!/bin/sh
FROM python:3.11-slim

WORKDIR /app

COPY nextcloud_file_watcher /app/nextcloud_file_watcher
COPY requirements.txt /app/
COPY run.sh /app/

RUN pip install --no-cache-dir -r requirements.txt \
 && chmod +x /app/run.sh

CMD ["/app/run.sh"]

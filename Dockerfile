FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh ./
COPY ../nextcloud_file_watcher ./nextcloud_file_watcher

RUN chmod +x run.sh

CMD [ "./run.sh" ]

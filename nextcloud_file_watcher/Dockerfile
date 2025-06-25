FROM python:3.11-slim

WORKDIR /app

COPY briefkasten_watcher.py /app/
COPY config.json /app/

RUN pip install requests

CMD ["python", "/app/briefkasten_watcher.py"]


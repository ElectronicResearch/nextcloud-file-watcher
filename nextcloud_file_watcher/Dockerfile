FROM python:3.11-slim

RUN pip install --no-cache-dir -r /requirements.txt

COPY briefkasten_watcher.py /briefkasten_watcher.py
CMD ["python3", "/briefkasten_watcher.py"]

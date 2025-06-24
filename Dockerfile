FROM python:3.11-slim

WORKDIR /app

COPY briefkasten_watcher.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/briefkasten_watcher.py"]

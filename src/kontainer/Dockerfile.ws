FROM python:3.12-slim

WORKDIR /app
COPY src/ ./src/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3002
CMD ["python", "-m", "src.api.websocket"]

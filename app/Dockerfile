FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser && chown -R appuser:appuser /app

COPY . .

RUN rm Dockerfile

USER appuser

EXPOSE 5000

CMD ["python", "flask_server.py"]


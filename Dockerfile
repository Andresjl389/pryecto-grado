FROM python:3.10-slim

# Instala bash y curl usando APT (no APK)
RUN apt-get update && apt-get install -y bash curl && rm -rf /var/lib/apt/lists/*

# Descarga wait-for-it
RUN curl -sSL https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh -o /wait-for-it.sh && \
    chmod +x /wait-for-it.sh

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

EXPOSE 8080

CMD ["/wait-for-it.sh", "db:5432", "--", "sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8080"]

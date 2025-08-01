# 1. Python base image
FROM python:3.10-slim

# 2. Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# 3. Gereken dosyaları kopyala
COPY . .

# 4. Gerekli paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Uvicorn ile başlat
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

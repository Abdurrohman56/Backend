# Gunakan image dasar resmi Python
FROM python:3.9-slim

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Buat direktori kerja
WORKDIR /app

# Salin file requirements.txt ke dalam image
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Salin seluruh kode aplikasi ke dalam image
COPY . /app/

# Ekspose port yang akan digunakan oleh aplikasi Flask
EXPOSE 5000

# Jalankan aplikasi menggunakan Gun

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

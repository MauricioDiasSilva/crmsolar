#!/bin/sh

echo "Aguardando o MySQL iniciar..."
while ! nc -z db 3306; do
  sleep 2
done
echo "MySQL iniciado!"

# Garante que o diretório de trabalho está certo
cd /app

# Gera e aplica migrations
python manage.py makemigrations
python manage.py migrate

# Inicia o servidor Django
exec python manage.py runserver 0.0.0.0:8000

#!/bin/sh

# Executa as migrações do banco de dados
python manage.py migrate

# Cria o superusuário se ele não existir
python manage.py create_superuser

# Inicia a aplicação
gunicorn --bind 0.0.0.0:8000 energy.wsgi
# Usamos la imagen oficial de Python
FROM python:3.10

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Instalar Node.js y npm
RUN apt-get update && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# Verificar la instalación de Node.js y npm
RUN node -v && npm -v

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    python3-dev

# Copiar los archivos al contenedor
COPY requirements.txt requirements.txt

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY . .

# Comando por defecto para ejecutar Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]


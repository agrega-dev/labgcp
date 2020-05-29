FROM python:3.7-slim

# Instalar todas las dependencias de nuestro codigo
RUN pip install Flask gunicorn Jinja2 requests Werkzeug lxml httplib2


# Copiamos el codigo a la imagen del contenedor
WORKDIR /app
COPY . .

ENV PORT 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 main:app

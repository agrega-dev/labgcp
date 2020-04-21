# Instalar python, pip y virtualenv
apt-get update
apt-get install -yq git supervisor python python-pip
pip install --upgrade pip virtualenv

# crear usuario para la aplicación
useradd -m -d /home/pythonapp pythonapp

#  Clonar aplicación desde GITHUB en servidor
export HOME=/root
git clone https://github.com/agrega-dev/labgcp.git /opt/app

# Preparar ambiente de python
virtualenv -p python3 /opt/app/gce/env
source /opt/app/gce/env/bin/activate
/opt/app/gce/env/bin/pip install -r /opt/app/gce/requirements.txt

# Otorgar privilegios al usuario sobre el directorio donde se encuentra la aplicación
chown -R pythonapp:pythonapp /opt/app

# Colocar el archivo de configuración de supervisor en el lugar correcto 
cp /opt/app/gce/python-app.conf /etc/supervisor/conf.d/python-app.conf

# iniciar servicios de supervisor
supervisorctl reread
supervisorctl update

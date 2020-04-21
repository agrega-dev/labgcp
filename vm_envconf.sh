# Instalar python, pip y virtualenv
sudo apt-get update
sudo apt-get install -yq git supervisor python python-pip
sudo pip install --upgrade pip virtualenv

# crear usuario para la aplicación
sudo useradd -m -d /home/pythonapp pythonapp

#  Clonar aplicación desde GITHUB en servidor
export HOME=/root
sudo git clone https://github.com/agrega-dev/labgcp.git /opt/app

# Preparar ambiente de python
sudo virtualenv -p python3 /opt/app/labgcp/env
sudo source /opt/app/labgcp/env/bin/activate
sudo /opt/app/gce/labgcp/bin/pip install -r /opt/app/labgcp/requirements.txt

# Otorgar privilegios al usuario sobre el directorio donde se encuentra la aplicación
sudo chown -R pythonapp:pythonapp /opt/app

# Colocar el archivo de configuración de supervisor en el lugar correcto 
sudo cp /opt/app/labgcp/python-app.conf /etc/supervisor/conf.d/python-app.conf

# iniciar servicios de supervisor
sudo supervisorctl reread
sudo supervisorctl update

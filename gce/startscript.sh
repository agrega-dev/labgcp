# Instalar python, pip y virtualenv
sudo apt-get update
apt-get update
apt remove python
apt-get install -yq git python3 python3-pip python3-setuptools build-essential

# crear usuario para la aplicación
sudo useradd -m -d /home/pythonapp pythonapp

#  Clonar aplicación desde GITHUB en servidor
export HOME=/root
sudo git clone https://github.com/agrega-dev/labgcp.git /opt/app/labgcp

# Preparar ambiente de python
pip3 install -r /opt/app/requirements.txt

# Otorgar privilegios al usuario sobre el directorio donde se encuentra la aplicación
sudo chown -R pythonapp:pythonapp /opt/app
cd /opt/app

# Levantar aplicación 
gunicorn -w 15 -b 0.0.0.0:3000 main:app -D

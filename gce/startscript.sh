apt-get update
apt remove python
apt-get install -yq git python3 python3-pip python3-setuptools build-essential nginx
pip3 install flask

useradd -m -d /home/pythonapp pythonapp

HOME=/root
git clone https://github.com/agrega-dev/labgcp.git /opt/app

pip3 install -r /opt/app/requirements.txt

chown -R pythonapp:pythonapp /opt/app
cd /opt/app
gunicorn -w 15 -b 0.0.0.0:3000 main:app -D
mv /opt/app/nginx/default /etc/nginx/sites-available/default
service nginx restart

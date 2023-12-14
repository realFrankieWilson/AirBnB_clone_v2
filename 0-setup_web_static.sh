#!/usr/bin/env bash
# A bash script that sets up web servers for the deployment of web_static

# Nginx Installation
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create Directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# HTML Contents
sudo bash -c 'cat << EOF > /data/web_static/releases/test/index.html
<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
</body>
EOF'

# Creates a Link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give the necessary permision
chown -R ubuntu:ubuntu /data/

# Configuration file
config="\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}"
sudo sed -i "29 i\\
$config" /etc/nginx/sites-available/default

# Restart nginx service
sudo service nginx restart

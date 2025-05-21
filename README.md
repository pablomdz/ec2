Descripcion: Script permite saturar la memoria de la instancia EC2. Esta funcion permite cambiar el porcentaje de memoria

Al crear la instancia se debe agregar las siguientes lineas:
#!/bin/bash

# Descargar el archivo de Python desde el repositorio
wget https://raw.githubusercontent.com/pablomdz/ec2/refs/heads/main/stress2.py

# Instalar pip mediante yum
sudo yum install -y python3-pip

# Instalar Flask con pip3
sudo pip3 install flask

# Instalar psutil con pip3
sudo pip3 install psutil

# Ejecutar el script de Python
sudo python3 stress2.py

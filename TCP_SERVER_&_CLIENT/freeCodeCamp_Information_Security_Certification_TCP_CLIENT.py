# Python for Penetration Testing -- Information Security Certification from freeCodeCamp
# https://github.com/Fertry/freeCodeCamp_Information_Security_Certification
# This file is a TCP CLIENT

import socket

# Definimos el objeto 'serverSocket'
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definimos un host y un puerto
host = socket.gethostname()
port = 444

# Conectamos con el servidor
clientSocket.connect((host, port))

# Definimos el maximo de datos a enviar
message = clientSocket.recv(1024)

# Cerramos la conexion
clientSocket.close()

print(message.decode('ascii'))

# Python for Penetration Testing -- Information Security Certification from freeCodeCamp
# https://github.com/Fertry/freeCodeCamp_Information_Security_Certification
# This file is a TCP SERVER

# Librerias importadas
import socket

# Definimos el objeto 'serverSocket'
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definimos un host y un puerto
host = socket.gethostname()
port = 444

# Bindeamos el host y el puerto al objeto
serverSocket.bind((host, port))

# 'Escuchamos' hasta 5 conexiones del host por el puerto especificado
serverSocket.listen(5)

# Bucle de ejecución
while(True):
    
    clientSocket, address = serverSocket.accept()
    
    # Confirmamos que la conexion está establecida
    print("Received connection from " + str(address))

    # Definimos un mensaje para enviar
    message = "Thank you for connecting to the server. This is an example of how sockets work." + "\r\n"

    # Enviamos el mensaje al host por el puerto especificado
    clientSocket.send(message.encode('ascii'))

    # Cerramos la conexion
    clientSocket.close()

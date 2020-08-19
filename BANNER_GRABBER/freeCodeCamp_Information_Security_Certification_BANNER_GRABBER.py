# Python for Penetration Testing -- Information Security Certification from freeCodeCamp
# https://github.com/Fertry/freeCodeCamp_Information_Security_Certification
# This file is a BANNER GRABBER

import socket

# Función banner
def banner(ip, port):

    # Declaramos un objeto de tipo 'socket'
    sck = socket.socket()
    # Iniciamos la conexión a la IP y puerto especificado
    sck.connect((ip, int(port)))
    # Declaramos un tiempo de espera de 20 segundos
    sck.settimeout(20)
    print(sck.recv(1024))

# Función main
def main():

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    ip = input("Please input an IP address: ")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    port = input("Please input a PORT: ")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    banner(ip, port)

# Bucle principal
if __name__ == "__main__":

    main()

# Python for Penetration Testing -- Information Security Certification from freeCodeCamp
# https://github.com/Fertry/freeCodeCamp_Information_Security_Certification
# This file is a PORT SCANNER

import socket

# Objeto de tipo 'socket'
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Función portScanner
def portScanner(port, host):

    if sck.connect_ex((host, port)):
        print("The port " + str(port) + " is closed")
    else:
        print("The port " + str(port) + " is open")

# Función principal
def main():

    # Tomamos un puerto para escanear
    print("<------------------------------>")
    prt = input("Please provide a port: ")
    # Tomamos una IP para escanear
    hst = input("Please provide an IP: ")
    print("<------------------------------>")
    print("You entered port: " + str(prt))    
    print("You entered IP: " + str(hst))
    print("<------------------------------>")
    # Llamamos a portScanner()
    portScanner(int(prt), hst)

# Bucle principal
if __name__ == "__main__":

    main()

# Python for Penetration Testing -- Information Security Certification from freeCodeCamp
# https://github.com/Fertry/freeCodeCamp_Information_Security_Certification
# This file is a NMAP SCANNER

import nmap

# Definimos el objeto 'scanner'
scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------->")

# Solicitamos una dirección IP
ipAddress = input("Please provide a IP address to scan: ")
print("The IP you entered is: " + str(ipAddress))
type(ipAddress)

# Bucle de ejecución
while True:

    # 3 tipos de scan para elegir:
    resp = input("""\n Please enter the type of scan to run
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Comprehensive Scan
                \n""")
    print("You have selected option: " + resp)  
    print("<-------------------------------------------->")                 

    if resp == '1':
        print("################################################################")
        print("Nmap Version: " + str(scanner.nmap_version))
        scanner.scan(ipAddress, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("IP Status: " + str(scanner[ipAddress].state()))
        print(scanner[ipAddress].all_protocols())
        print("Open Ports: " + str(scanner[ipAddress]['tcp'].keys()))
        print("################################################################")

    elif resp == '2':
        print("################################################################")
        print("Nmap Version: " + str(scanner.nmap_version))
        scanner.scan(ipAddress, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("IP Status: " + str(scanner[ipAddress].state()))
        print(scanner[ipAddress].all_protocols())
        print("Open Ports: " + str(scanner[ipAddress]['udp'].keys()))
        print("################################################################")

    elif resp == '3':
        print("################################################################")
        print("Nmap Version: " + str(scanner.nmap_version))
        scanner.scan(ipAddress, '1-1024', '-v -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("IP Status: " + str(scanner[ipAddress].state()))
        print(scanner[ipAddress].all_protocols())
        print("Open Ports: " + str(scanner[ipAddress]['tcp'].keys()))
        print("################################################################")

    else:
        print("Please enter a valid option")

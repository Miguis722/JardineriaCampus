import os
from tabulate import tabulate
import requests

#Servidor de Oficina
def getAllDataOficina():
    peticion = requests.get("http://172.16.106.120:5005")
    data = peticion.json()
    return data

#Devuelve un listado con el código de
#Oficina y la ciudad donde hay oficinas

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllDataOficina():
        codigoCiudad.append({
            "Ciudad": val.get('ciudad'),
            "Codigo de Oficina": val.get('codigo_oficina')
        })
    return codigoCiudad
#Devuelve un listado con la ciudad y el teléfono de las
#oficinas de España.

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in getAllDataOficina():
        if(val.get('pais') == pais):
            ciudadTelefono.append({
                "Pais": val.get('pais'),
                "Ciudad": val.get('ciudad'),
                "Telefono": val.get('telefono'),
                "Codigo de Oficina": val.get('codigo_oficina')
            })
    return ciudadTelefono
#Devuelve un listado de la información introduciendo el codigo Postal


def getAllCodigoPostal(codigoPostalBuscado):
    codigosPostalesEncontrados = []
    for val in getAllDataOficina():
        if val.get('codigo_postal') == codigoPostalBuscado:
            codigosPostalesEncontrados.append({ 
                "Codigo de Oficina": val.get('codigo_oficina'),
                "Region": val.get('region'),
                "telefono": val.get('telefono'),
                "Dirección": val.get('linea_direccion1')
                })
    return codigosPostalesEncontrados


def menu():
    os.system('clear')
    print("""

          


 _______                                  _                 __                    ___  _           _                 
|_   __ \                                / |_              |  ]                 .' ..](_)         (_)                
  | |__) |  .---. _ .--.    .--.  _ .--.`| |-'.---.    .--.| | .---.    .--.   _| |_  __   .---.  __  _ .--.  ,--.   
  |  __ /  / /__\[ '/'`\ \/ .'`\ [ `/'`\]| | / /__\\ / /'`\' |/ /__\\ / .'`\ \'-| |-'[  | / /'`\][  |[ `.-. |`'_\ :  
 _| |  \ \_| \__.,| \__/ || \__. || |    | |,| \__., | \__/  || \__., | \__. |  | |   | | | \__.  | | | | | |// | |, 
|____| |___|'.__.'| ;.__/  '.__.'[___]   \__/ '.__.'  '.__.;__]'.__.'  '.__.'  [___] [___]'.___.'[___|___||__]'-;__/ 
                 [__|                                                                                                
                                          
          
        1. Obtener las ubicaciones de una oficina en determinada ciudad
        2. Obtener los datos las oficinas en un pais (Ejemplo: España).
        3. Obtener la información de la persona por su codigo Postal.
        Si desea volver, precione la tecla: Esc
          
""")
    opcion = int(input("\nIngrese la opcion que desea realizar: "))
    if(opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 2):
        pais = input("Ingrese el pais: ")
        print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 3):
        codigoPostal = input("Ingrese el codigo Postal: ")
        print(tabulate(getAllCodigoPostal(codigoPostal), headers="keys", tablefmt="fancy_grid"))
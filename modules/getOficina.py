from tabulate import tabulate
import Storage.oficina as of
#Devuelve un listado con el código de
#Oficina y la ciudad donde hay oficinas

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo_oficina": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad
#Devuelve un listado con la ciudad y el teléfono de las
#oficinas de España.

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas": val.get("codigo_oficina"),
                "pais": val.get("pais")
            })
    return ciudadTelefono

def menu():
    print("""
______                      _             _               __ _      _             
| ___ \                    | |           | |             / _(_)    (_)            
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___    ___ | |_ _  ___ _ _ __   __ _ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \  / _ \|  _| |/ __| | '_ \ / _` |
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | (_) | | | | (__| | | | | (_| |
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___|  \___/|_| |_|\___|_|_| |_|\__,_|
          | |                                                                     
          |_|                                                                    
          
        1. Obtener las ubicaciones de una oficina en determinada ciudad (codigo de la oficina y ciudad)
        2. Obtener los datos las oficinas en un pais (pais)
""")
    opcion = int(input("\nIngrese la opcion que desea realizar: "))
    if(opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 2):
        pais = input("Ingrese el pais: ")
        print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="fancy_grid"))
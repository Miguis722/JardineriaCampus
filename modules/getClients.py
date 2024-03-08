from tabulate import tabulate
import Storage.cliente as cli

def getAllClienteName():
    clienteNames = list()
    for val in cli.clientes:
    #No es necesario poner indice y enumerate
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
        clienteNames.append(codigoName)
    return clienteNames
#Estamos pidiendo solamente los nombres de las personas

def getOneClienteCodigo(codigo):
    for val in cli.clientes:  
        if(val.get('codigo_cliente') == codigo):
            return({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
#Aqui haremos que solo nos de un nombre por codigo

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append({
                "Codigo": val.get('codigo_cliente'),
                "Responsable": val.get('nombre_cliente'),
                "Director": f"{val.get('nombre_contacto')} {val.get('nombre_contacto')}",
                "Telefono": val.get("telefono"),
                "Fax": val.get('fax'),
                "Direcciones": f"{val.get('pais')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                "Credito": val.get('limite_credito')
            })
    return clienteCredic
#Filtro que nos cuele solamente el limite crediticio y la ciudad especifica.

def getAllClientePaisRegionCiudad(pais,region=None, ciudad=None):
    #Si se pone =None, no es necesario que se ponga
    clientZone = list()
    for val in cli.clientes:
        if(
            val.get('pais') == pais and
            (val.get('region')== region or val.get('region') == None) or
            #Si se usase and, y este no se cumple, daria error y por consiguiente no saldria nada.
            (val.get('ciudad')== ciudad or val.get('ciudad') == None)
            ):
            
            clientZone.append(val)
            
    return clientZone


def getAllClientCiudad(ciudad):
    clientCiud = list()
    for val in cli.clientes:
        if(val.get('ciudad')== ciudad or val.get("ciudad") == None):
            clientCiud.append(val)
    return clientCiud

def getAllClientDireccion1():
    clientDireccion1 = list()
    for val in cli.clientes:
        direccion1 = dict({
            "codigo_cliente": val.get("codigo_cliente"),
            "nombre_cliente": val.get("nombre_cliente"),
            "linea_direccion1": val.get("linea_direccion1")
        })
        clientDireccion1.append(direccion1)
    return clientDireccion1

def getAllClientTelefono():
    clientTelefono = list()
    for val in cli.clientes:
        telefono = dict({
            "codigo_cliente": val.get("codigo_cliente"),
            "nombre_cliente": val.get("nombre_cliente"),
            "telefonos": val.get("telefono")
        })
        clientTelefono.append(telefono)
    return clientTelefono

def getAllClientFax():
    clientFar = list()
    for val in cli.clientes:
        fax = dict({
            "nombre_cliente": val.get("nombre_cliente"),
            "fax": val.get("fax")
        })
        clientFar.append(fax)
    return clientFar


def menu():
    print("""


______                      _             _        _                  _ _            _            
| ___ \                    | |           | |      | |                | (_)          | |           
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | | ___  ___    ___| |_  ___ _ __ | |_ ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ | |/ _ \/ __|  / __| | |/ _ \ '_ \| __/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | | (_) \__ \ | (__| | |  __/ | | | ||  __/\__ \
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| |_|\___/|___/  \___|_|_|\___|_| |_|\__\___||___/
          | |                                                                                     
          |_|                                                                                     

        1. Obtener todos los cientes (codigo y nombre)
        2. Obtener un cliente por el codigo (codigo y nombre)
        3. Obtener toda la información de un cliente según su limite de credito y ciudad que pertenece (ejemplo: 3000.0, San Francisco)
          
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllClienteName(),headers="keys", tablefmt="rounded_grid"))
    if(opcion == 2):
        codigoCliente = int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getOneClienteCodigo(codigoCliente),headers="keys",tablefmt="rounded_grid"))
    if(opcion == 3):
        codigoCliente = int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getAllClientCreditCiudad(codigoCliente), headers="keys", tablefmt="rounded_grid"))
    if(opcion == 4):
        ciudad = input("Ingrese la ciudad del cliente: ")
        print(tabulate(getAllClientCiudad(ciudad), headers="keys", tablefmt="rounded_grid"))
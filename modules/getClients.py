import os
from tabulate import tabulate
import requests
import json

#json-server storage/producto.json -b 5001

# http://154.38.171.54:5002/detalle_pedido

#Servidor de Pagos
def getAllDataPagos():
	peticion = requests.get("http://154.38.171.54:5006/pagos")
	data= peticion.json()
	return data

#Servidor de clientes
def getAllDataClientes():
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

#Servidor de Empleados
def getAllDataEmpleados():
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data

#Obtener el nombre de todos los clientes.
def getAllClienteName():
    clienteNames = list()
    for val in getAllDataClientes():
    #No es necesario poner indice y enumerate
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
        clienteNames.append(codigoName)
    return clienteNames
#Estamos pidiendo solamente los nombres de las personas

#Obtener un cliente por el codigo
def getOneClienteCodigo(numero):
    ClienteCodigo = []
    for val in getAllDataClientes():  
        if (val.get('codigo_cliente') == numero): 
            ClienteCodigo.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
    return ClienteCodigo
   
#Aqui haremos que solo nos de un nombre por codigo

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredicCiudad = []  
    for val in getAllDataClientes():
        limite_credito = float(val.get('limite_credito'))
        if limite_credito >= float(limiteCredit) and val.get('ciudad') == ciudad:
            clienteCredicCiudad.append({
                "Codigo": val.get('codigo_cliente'),
                "Responsable": val.get('nombre_cliente'),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Telefono": val.get('telefono'),
                "Fax": val.get('fax'),
                "Direcciones": f"{val.get('pais')} {val.get('direccion')}",
                "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                "Credito": limite_credito
            })
    return clienteCredicCiudad

#Filtro que nos cuele solamente el limite crediticio y la ciudad especifica.

def getAllClientePaisRegionCiudad(pais,region=None, ciudad=None):
    #Si se pone =None, no es necesario que se ponga
    clientZone = list()
    for val in getAllDataClientes():
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
    for val in getAllDataClientes():
        if(val.get('ciudad')== ciudad or val.get('ciudad') == None):
            clientCiud.append(val)
    return clientCiud

def getAllClientDireccion1():
    clientDireccion1 = list()
    for val in getAllDataClientes():
        direccion1 = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
            "linea_direccion1": val.get('linea_direccion1')
        })
        clientDireccion1.append(direccion1)
    return clientDireccion1

def getAllClientTelefono():
    clientTelefono = list()
    for val in getAllDataClientes():
        telefono = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
            "telefonos": val.get('telefono')
        })
        clientTelefono.append(telefono)
    return clientTelefono

def getAllClientFax():
    clientFar = list()
    for val in getAllDataClientes():
        fax = dict({
            "nombre_cliente": val.get('nombre_cliente'),
            "fax": val.get('fax')
        })
        clientFar.append(fax)
    return clientFar

#Devuelve un listado con todos los clientes que sean de la ciudad de Madrid y cuyo representante de ventas 
#Tenga el código de empleado 11 o 30.

def getAllClientesDeMadrid():
    ClientesDeMadrid = []
    for val in getAllDataClientes():
        if(val.get('ciudad') == 'Madrid') and val.get('codigo_empleado_rep_ventas') == 11 or 30:
            ClientesDeMadrid.append({
                "Código del cliente" : val.get('codigo_cliente'),
                "Nombre del cliente" : val.get('nombre_cliente'),
                "Apellidos del cliente": val.get('apellido_contacto'),
                "Pais - ciudad": val.get('pais') + "- " + val.get('ciudad')
            })
    return  ClientesDeMadrid

#1. Obten un listado con el nombre de cada cliente, y el nombre y apellido de su representante de ventas.

def getAllInformacionclienteAndRepresentante ():
    infoClienteYRepVentas = []
    for val in getAllDataClientes(), getAllDataEmpleados():
        if(val.get('codigo_empleado_rep_ventas') == val.get('codigo_empleado') and val.get('puesto') == "Representante Ventas"):
            infoClienteYRepVentas.append({
                "Nombre del cliente" : val.get('nombre_cliente'),
                "Apellidos del Cliente": val.get('apellido_contacto'),
                "Nombre del Representante de ventas": val.get('nombre')
            })
    return infoClienteYRepVentas
#2. Muestra el nombre de los clientes que hayan realizado los pagos junto con el nombre de sus representantes de ventas.

def getAllClientesPagoRealizadoRepresentantedeventas ():
    ClientesPagoRealizadoRepresentantedeventas = []
    for val in getAllDataClientes(),  getAllDataPagos(), getAllDataEmpleados():
        if val.get('estado') == "Entregado" or "Pendiente" and val.get('codigo_empleado_rep_ventas') == val.get('codigo_empleado'):
            ClientesPagoRealizadoRepresentantedeventas.append({
            "Nombre del Cliente": val.get('nombre_cliente'),
            "Nombre del representante de ventas": val.get('nombre') + ('apellido1') + ('apellido2')
                })
            
    return ClientesPagoRealizadoRepresentantedeventas

#3. Muestra el nombre de los clientes que no han realizado los pagos junto con el nombre de sus representates de ventas.





def menu():
    while True:
        os.system("cls")
        print("""


    ____                        __              __        _________            __           
   / __ \___  ____  ____  _____/ /____     ____/ /__     / ____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / /   / / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / /___/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/   \____/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                               
                                                         

        1. Obtener todos los cientes (codigo y nombre)
        2. Obtener un cliente por el codigo (codigo y nombre)
        3. Obtener toda la información de un cliente según su limite de credito y ciudad que pertenece (ejemplo: 3000.0, San Francisco)
        4. Obtener toda la información de un cliente por medio de su ciudad
        5. Obtener toda la información de clientes en España y que estos tengan el representante de ventar codigo de 11 o 30
        
        Si desea volver, precione: 0
          
""")
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllDataClientes(),headers="keys", tablefmt="rounded_grid"))
            input("Volver al menú: ")
        elif(opcion == 2):
            numero = int(input("Ingrese el codigo del cliente: "))
            print(tabulate(getOneClienteCodigo(numero),headers="keys",tablefmt="rounded_grid"))
            
        elif(opcion == 3):
            limiteCredit = (input("Ingrese el limite de credito: "))
            ciudad = (input("Ingrese la ciudad a la que pertenece: "))
            print(tabulate(getAllClientCreditCiudad(limiteCredit, ciudad), headers="keys", tablefmt="rounded_grid"))
            
        elif(opcion == 4):
            ciudad = input("Ingrese la ciudad del cliente: ")
            print(tabulate(getAllClientCiudad(ciudad), headers="keys", tablefmt="rounded_grid"))    
        elif(opcion ==5):
            print(tabulate(getAllClientesDeMadrid(), headers="keys", tablefmt="rounded_grid")) 
        elif (opcion == 0):
            break
    input("Si desea volver, presione: 0")

#GET CLIENTS : SOLUCIONADO Y DESARROLLADO EN SU TOTALIDAD, SI FUNCIONA, NO SE TOCA.
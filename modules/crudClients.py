import json
import os
import re
import requests
from tabulate import tabulate
import Procesosdetextos as Procedimientos
#Para facilitarnos estar nombrando los procesos uno por uno en cada uno de los documentos, ponemos un solo documento
#Y lo importaremos cada que lo necesitemos.



#Servidor de clientes - De aqui sacaremos y agregaremos toda la data/información necesaria
def getAllDataClientes():
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

#Aqui hara que cuando agreguemos a un nuevo cliente, se agregue un id, y se le agregue un nuevo ID.
def nuevoInfoCliente():
    codigoDelCliente = list()
    for val in getAllDataClientes():
        codigoCliente = val.get('codigo_cliente')
        if codigoCliente is not None:
            codigoDelCliente.append(codigoCliente)
    if codigoDelCliente:
        return max(codigoDelCliente) + 1
    else:
        return 1


#Deseamos agregar la información de un nuevo cliente, asignandole automaticamente un nuevo número de ID
def AddInfoClientes():

    print('Los datos no obligatorios se saltan digitando la tecla "n" mayuscula. (N)')
    cliente = {}
    while True:
        try:
            if not cliente.get('codigo_cliente'):
                
                codigo = input('Ingrese el codigo del cliente: ')
                #Ponemos que tienen que ponerse solo números de 0 a 9 (numeros enteros)
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    datas = getAllDataClientes(codigo)
                    if datas:
                        print(tabulate(datas, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El código del cliente ingresado ya existe, por favor verifique.")
                    else:
                        codigo = int(codigo)
                        cliente["codigo_cliente"] = codigo
                else: 
                    raise Exception("El código  del producto ingresado, no cumple con los parametros establecidos.")
            if not cliente.get("nombre_cliente"):
                
                nombre = input("Ingrese el nombre del cliente: ")
                #Agregamos caracteres especiales como el uso de las tildes y las Ñ
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", nombre) is not None):
                    cliente["nombre_cliente"] = nombre
                else:
                    raise Exception ("El nombre del cliente ingresado, no cumple con los parametros establecidos, por favor verifique.")
            if not cliente.get("nombre_contacto"):
                
                nombre_contacto = input("Ingrese el nombre de contacto del cliente: ")
                #Agregamos caracteres especiales como el uso de las tildes y las Ñ
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", nombre_contacto) is not None):
                    cliente["nombre_contacto"] = nombre_contacto
                else:
                    raise Exception ("El nombre de contacto del cliente ingresado, no cumple con los parametros establecidos, porfavor verifique.")
            if not cliente.get("apellido_contacto"):
                
                apellido_contacto = input("Ingrese el apellido del cliente: ")
                #Agregamos caracteres especiales como el uso de las tildes y las Ñ
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", apellido_contacto) is not None):
                    cliente["apellido_contacto"] = apellido_contacto
                else:
                    raise Exception ("El apellido de contacto del cliente ingresado, no cumple con los parametros establecidos, por favor verifuqye.")
            if not cliente.get("telefono"):
                
                telefono = input("Ingrese el telefono del cliente: ")
                #Ponemos que tienen que ponerse solo números de 0 a 9 (numeros enteros)
                if(re.match(r"^[0-9\s-]+$", telefono) is not None):
                    #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    cliente["telefono"] = telefono
                else:
                    raise Exception ("El telefono de contacto del cliente ingresado, no cumple con los parametros establecidos, por favor verifuique.")
            if not cliente.get("fax"):
                
                fax = input("Ingrese el fax del cliente: ")
                #Ponemos que tienen que ponerse solo números de 0 a 9 (numeros enteros)
                if(re.match(r"^[0-9\s-]+$", fax) is not None):
                    #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    cliente["fax"] = fax
                else:
                    raise Exception ("El fax del cliente ingresado, no cumple con los parametros establecidos, porfavor verifique.")
            if not cliente.get("linea_direccion1"):
                linea_direccion1 = input("Ingrese la direccion 1 del cliente: ")
                cliente["linea_direccion1"] = linea_direccion1
            if not cliente.get("linea_direccion2"):
                linea_direccion2 = input("Ingrese la direccion 2 del cliente: ")
                cliente["linea_direccion2"] = linea_direccion2
            if not cliente.get("ciudad"):
                
                ciudad = input("Ingrese la ciudad del cliente: ")
                #Agregamos caracteres especiales como el uso de las tildes y las Ñ
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", ciudad) is not None):
                    #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    cliente["ciudad"] = ciudad
                else:
                    raise Exception ("La ciudad del cliente ingresada, no cumple con los parametros establecidos, por favor verifique.")
            if not cliente.get("region"):
                region = input("Ingrese la region del cliente: ")
                if region == "N":
                    #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    cliente["region"] = region 
                    #Agregamos caracteres especiales como el uso de las tildes y las Ñ
                elif(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", region) is not None):
                    #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    cliente["region"] = region
                else:
                    raise Exception ("la region del cliente no cumple con los parametros")
            if not cliente.get("pais"):
                pais = input("Ingrese el pais del cliente: ")
                if pais == "N":
                    cliente["pais"] = pais #Futuramente None
                else:
                    #Agregamos caracteres especiales como el uso de las tildes y las Ñ
                    if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", pais) is not None):
                        #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                        cliente["pais"] = pais
                    else:
                        raise Exception ("el pais del cliente no cumple con los parametros")
            if not cliente.get("codigo_postal"):
                
                codigo_postal = input("Ingrese el codigo postal del cliente: ")
                #Ponemos que tienen que ponerse solo números de 0 a 9 (numeros enteros)
                if(re.match(r"^[0-9]+$", codigo_postal) is not None):
                    #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    cliente["codigo_postal"] = codigo_postal
                else:
                    raise Exception ("el codigo postal del cliente no cumple con los parametros")
            if not cliente.get("codigo_empleado_rep_ventas"):
                
                codigo_empleado_rep_ventas = input("Ingrese el codigo del empleado R.V. del cliente: ")
                #Ponemos que tienen que ponerse solo números de 0 a 9 (numeros enteros)
                if(re.match(r"^[0-9]+$", codigo_empleado_rep_ventas) is not None):
                #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                    cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
                else:
                    raise Exception ("El código del empleado R.V. del cliente no cumple con los parametros")
            if not cliente.get("limite_credito"):
                
                limite_credito = input("Ingrese el limite de crédito del cliente: ")
                #Ponemos que tienen que ponerse solo números de 0 a 9 (numeros enteros)
                if(re.match(r"^[0-9]+$", limite_credito) is not None):
                    #En cuyo caso, podemos dejar que se  quede vacia para no tener que preguntar
                    limite_credito = float(limite_credito)
                    cliente["limite_credito"] = limite_credito
                    break
                else:
                    raise Exception ("El limite de crédito del cliente no cumple con los parametros preestablecidos.")
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.103.39:5003/clientes",  headers=headers , data=json.dumps(cliente, indent=4))
    res = peticion.json()
    tablaCliente = [cliente]
    print(tabulate(tablaCliente, headers="keys", tablefmt="rounded_grid"))

#Deseamos eliminar la información de un cliente en especifico, por lo que usamos un delete UBICADO (ya borre la base de datos una vez por no tenerlo ubicado xd)
def deletClient(id):
    data = getAllDataClientes(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        peticion = peticion.json()
        if peticion.ok == 204:
            #204 = corresponde a contenido eliminado
            return print("Producto eliminado")
        else:
            return print("Producto no encontrado")

#Deseamos actualizar la información de un cliente en especifico
def updateCliente(id):
    data = getAllDataClientes(id)
    if(len(data)):
        cliente = dict()
        cliente["codigo_cliente"] = data["codigo_cliente"]
        while True:
            try:
                if(not cliente.get("nombre_cliente")):
                    nombreCliente = input("Ingrese el nombre del cliente: ")
                    if(Procedimientos.ValidacionDeNombre(nombreCliente) is not None):
                        cliente["nombre_cliente"] = nombreCliente
                    else:
                        raise Exception("El nombre del cliente no cumple con lo establecido")
                
                if(not cliente.get("nombre_contacto")):
                    nombreContacto = input("Ingrese el nombre del contacto: ")
                    if(Procedimientos.ValidacionDeNombre(nombreContacto) is not None):
                        cliente["nombre_contacto"] = nombreContacto
                    else:
                        raise Exception("El nombre del contacto no cumple con lo establecido")
                    
                if(not cliente.get("apellido_contacto")):
                    apellidoContacto = input("Ingrese el apellido de contacto: ")
                    if(Procedimientos.ValidacionDeNombre(apellidoContacto) is not None):
                        cliente["apellido_contacto"] = apellidoContacto
                    else:
                        raise Exception("El apellido del contacto no cumple con lo establecido")
                    
                if(not cliente.get("telefono")):
                    telefono = input("Ingrese el numero de telefono: ")
                    if(Procedimientos.ValidacionDeNumeros(telefono) is not None):
                        cliente["telefono"] = telefono
                    else:
                        raise Exception("El telefono ingresado no cumple con lo establecido")
                    
                if(not cliente.get("fax")):
                    fax = input("Ingrese el fax: ")
                    if(Procedimientos.ValidacionDeNumeros(fax) is not None):
                        cliente["fax"] = fax
                    else:
                        raise Exception("El fax ingresado no cumple con lo establecido")
                    
                if(not cliente.get("linea_direccion1")):
                    direccion1 = input("Ingrese una linea de direccion: ")
                    cliente["linea_direccion1"] = direccion1
                    
                direccion2 = input("Ingrese otra linea de direccion(opcional): ")
                if direccion2:
                    cliente["linea_direccion2"] = direccion2

                if(not cliente.get("ciudad")):
                    ciudad = input("Ingrese la ciudad: ")
                    if(Procedimientos.ValidacionDeNombre(ciudad) is not None):
                        cliente["ciudad"] = ciudad
                    else:
                        raise Exception("El nombre de la ciudad no cumple con lo establecido")

                region = input("Ingrese la region (opcional): ")
                if region:
                    if Procedimientos.ValidacionDeNombre(region) is not None:
                        cliente["region"] = region

                if(not cliente.get("pais")):
                    pais = input("Ingrese el pais: ")
                    if(Procedimientos.ValidacionDeNombre(pais) is not None):
                        cliente["pais"] = pais
                    else:
                        raise Exception("El nombre del pais no cumple con lo establecido")
                    
                if(not cliente.get("codigo_postal")):
                    codigoPostal = input("Ingrese el codigo postal: ")
                    if(Procedimientos.ValidacionDeNumeros(codigoPostal) is not None):
                        cliente["codigo_postal"] = codigoPostal
                    else:
                        raise Exception("El codigo postal no cumple con lo establecido")
                    
                if(not cliente.get("codigo_empleado_rep_ventas")):
                    codigoEmpleado = input("Ingrese el codigo de empleado: ")
                    if(Procedimientos.ValidacionDeNumeros(codigoEmpleado) is not None):
                        codigoEmpleado = int(codigoEmpleado)
                        cliente["codigo_empleado_rep_ventas"] = codigoEmpleado
                    else:
                        raise Exception("El codigo de empleado no cumple con lo establecido")
                    
                if(not cliente.get("limite_credito")):
                    limiteCredito = input("Ingrese el limite de credito: ")
                    if(Procedimientos.ValidacionDeNumeros(limiteCredito) is not None):
                        limiteCredito = int(limiteCredito)
                        cliente["limite_credito"] = limiteCredito
                        break
                    else:
                        raise Exception("El codigo de empleado no cumple con lo establecido")
                    
            except Exception as error:
                print(error)

        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", headers=headers, data=json.dumps(cliente))
        res = peticion.json()
        res["Mensaje"] = "Cliente Actualizado Correctamente"
        return [res]
    
    else:
        return[{
            "messege": "Producto no encontrado",
            "id": id
        }]






def menu():
    while True:
        os.system("cls")
        print(""" 

    ___       __          _       _      __                 __                  __             ___            __           
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /__     _____/ (_)__  ____  / /____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/____/  
                                                                                                                           

              1. Agregar información de un cliente nuevo
              2. Eliminar información de un cliente
              3. Modificar información del cliente

            Si desea volver, precione: 0

""")
        opcion = (input("\nSeleccione una de las opciones: "))
        if re.match(r'^[0-3]+$', opcion) is not None:
            opcion = int(opcion)
            if  opcion == 1:
                print(tabulate(AddInfoClientes()))
                input("Si desea volver, presione: 0")
                
            elif opcion == 2:
                id = int(input("Por favor, introduzca el id a eliminar: "))
                print(tabulate(deletClient(id)))
                input("Si desea volver, presione: 0")
            elif opcion == 3:
                input("Si desea volver, presione: 0")
                print("Que hubo")
            elif opcion == 0:
                break
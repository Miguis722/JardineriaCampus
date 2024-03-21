import json
import os
import re
import requests
from tabulate import tabulate
import Procesosdetextos as Procesos

#Servidor de pagos
def getAllDataPagos():
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data 

def getPagoCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{codigo}")
    return peticion.json() if peticion.ok else []

def getIdDelPago(id):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
    return [peticion.json()] if peticion.ok else[]



def AddDataPagos():
    pago ={}
    while True:
        try:
            if not pago.get("id_transaccion"):
                
                id_transaccion= input("Ingrese la id de la transaccion:  ")
                if(re.match(r"^[a-z0-9-]+$", id_transaccion) is not None):
                    datas = getPagoCodigo()
                    for val in datas:
                        
                        if val.get("id_transaccion") == id_transaccion:
                            print(tabulate(val, headers="keys", tablefmt="rounded_grid"))
                            raise Exception("El codigo del empleado ya existe")
                        else:
                            pago["id_transaccion"] = id_transaccion
                else:
                    raise Exception ("La id de la transaccion no cumple con los parametros")
            if not pago.get("codigo_cliente"):
                
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    codigo = int(codigo)
                    pago["codigo_cliente"] = codigo
                else:
                    raise Exception("El codigo del cliente no cumple con el estandar establecido")
            if not pago.get("forma_pago"):
                
                forma_pago = input("Ingrese la forma de pago: ")
                if(re.match(r"^[A-Za-z]+$", forma_pago) is not None):
                    pago["forma_pago"] = forma_pago
                else:
                    raise Exception ("La forma de pago no cumple con los parametros")
            if not pago.get("fecha_pago"):
                
                fecha_pago = input("Ingrese la fecha de pago: ")
                if(re.match(r"^[0-9-]+$", fecha_pago) is not None):
                    pago["fecha_pago"] = fecha_pago
                else:
                    raise Exception ("La fecha de pago no cumple con los parametros")
            if not pago.get("total"):
                
                total_pago = input("Ingrese el total del pago: ")
                if(re.match(r"^[0-9\s-]+$", total_pago) is not None):
                    pago["total"] = total_pago
                    break
                else:
                    raise Exception ("el total no cumple con los parametros")
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5006/pagos",  headers=headers , data=json.dumps(pago, indent=4))
    res = peticion.json()
    tablapago = [pago]
    print(tabulate(tablapago, headers="keys", tablefmt="rounded_grid"))

def deletePago(id):
    data = getIdDelPago(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        if peticion.status_code == 204:
            data.append({"message" : "El producto fue eliminado correctamente"})
            return{
                "body": data,
                "status" : peticion.status_code
            }
        else:
            return[{
                "body": {
                    "message" : "producto no encontrado",
                    "data" : id
                },
                "status" : 400
                }]

    
def updatePago(id):
    data = getPagoCodigo(id)
    if(len(data)):
        print("Pago Encontrado")
        print(tabulate([data], headers="keys", tablefmt="rounded_grid"))
        data["codigo_cliente"] = data["codigo_cliente"]
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Nombre 
                    2. Primer apellido
                    3. Segundo apellido
                    4. Extension
                    5. Email
                    6. Codigo de la oficina
                    7. Codigo jefe
                    8. Puesto
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(Procesos.ValidacionDeNumeros(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 8):
                        if(opcion == 1):
                            while True:
                                try:
                                    formaPago = input("Ingrese la forma de pago: ")
                                    if(Procesos.ValidacionDeNombre(formaPago) is not None):
                                        data["forma_pago"] = formaPago
                                        break
                                    else:
                                        raise Exception("La forma de pago no cumple con lo establecido")  
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    idTransaccion = input("Ingrese la id de la transaccion: ")
                                    if(Procesos.Validaciondetransacciones(idTransaccion) is not None):
                                        data["id_transaccion"] = idTransaccion
                                        break
                                    else:
                                        raise Exception("La id de la transaccion no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    fechaPago = input("Ingrese la fecha de pago: ")
                                    if(Procesos.ValidacionDeFecha(fechaPago) is not None):
                                        data["fecha_pago"] = fechaPago
                                        break
                                    else:
                                        raise Exception("La fehca no cumple con lo establecido") 
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    total = input("Ingrese el total del pago: ")
                                    if(Procesos.validacionDeNumeros(total) is not None):
                                        total = int(total)
                                        data["total"] = total
                                        break
                                    else:
                                        raise Exception("El pago no cumple con lo establecido")   
                                except Exception as error:
                                    print(error)
                        

                        confirmacion = ""            
                        while (confirmacion !=  "s" and confirmacion != "n"):
                            confirmacion = input("Deseas cambiar mas datos?(s/n): ")
                            if Procesos.ValidacionSiNo(confirmacion):
                                if confirmacion == "n":
                                    continuarActualizar = False
                                    break
                                else:
                                    confirmacion == "s"
                                    break
                            else:
                                print("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
        
        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        return [res]
    else:
        return[{
            "messege": "Pago no encontrado",
            "id": id
        }]
def menu():
    while True:
        os.system("cls")  
        print("""


    __  ___             __         __        ____                        
   /  |/  /__  ____  __/_/_   ____/ /__     / __ \____ _____ _____  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / /_/ / __ `/ __ `/ __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / ____/ /_/ / /_/ / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_/    \__,_/\__, /\____/____/  
                                                     /____/              

        
          
          1. Agregar información de un pago nuevo
          2. Eliminar información de un pago ya existente
          3. Actualizar información de un pago ya existente

    """)
        
        opcion = input("\nSeleccione una de las opciones: ")
        if(Procesos.ValidacionDeNumeros(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):
                if (opcion == 1):
                    print(tabulate(AddDataPagos(), headers="keys", tablefmt="rounded_grid"))
                    input("Si desea volver, presione: 0")
                elif (opcion == 2):
                    id = int(input("Ingrese el codigo del pago que deseas eliminar: "))
                    print(tabulate(deletePago(id), tablefmt="rounded_grid"))
                    input("Si desea volver, presione: 0")
                elif (opcion == 3):
                    id = int(input("Ingrese el codigo del pago que deseas actualizar: "))
                    print(tabulate(updatePago(id), headers="keys", tablefmt="rounded_grid"))
                    input("Si desea volver, presione: 0")
                elif (opcion == 0):
                    break
            


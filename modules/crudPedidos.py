import json
import os
import re
import requests
from tabulate import tabulate
import Procesosdetextos as Procesos

#Servidor de Pagos
def getAllDataPago():
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data

#Obtener el codigo del pago realizado o a realizar
def getCodigoPago():
    peticion = requests.get(f"http://154.38.171.54:5006/pagos")
    return [peticion.json()] if peticion.ok else[]

def getIdPago(id):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
    return [peticion.json()] if peticion.ok else[]

#Deseamos agregar información de los pagos
def AddInfoPagos():
    pago ={}
    while True:
        try:
            if not pago.get("id_transaccion"):
                
                id_transaccion= input("Ingrese la id de la transaccion:  ")
                if(re.match(r"^[a-z0-9-]+$", id_transaccion) is not None):
                    datas=getCodigoPago()
                    for val in datas:
                        
                        if val.get("id_transaccion") == id_transaccion:
                            print(tabulate(val, headers="keys", tablefmt="github"))
                            raise Exception("el codigo del empleado ya existe")
                        else:
                            pago["id_transaccion"] = id_transaccion
                else:
                    raise Exception ("la id de la transaccion no cumple con los parametros")
            if not pago.get("codigo_cliente"):
                
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    codigo = int(codigo)
                    pago["codigo_cliente"] = codigo
                else:
                    raise Exception("el codigo del cliente no cumple con el estandar establecido")
            if not pago.get("forma_pago"):
                
                forma_pago = input("Ingrese la forma de pago: ")
                if(re.match(r"^[A-Za-z]+$", forma_pago) is not None):
                    pago["forma_pago"] = forma_pago
                else:
                    raise Exception ("la forma de pago no cumple con los parametros")
            if not pago.get("fecha_pago"):
                
                fecha_pago = input("Ingrese la fecha de pago: ")
                if(re.match(r"^[0-9-]+$", fecha_pago) is not None):
                    pago["fecha_pago"] = fecha_pago
                else:
                    raise Exception ("la fecha de pago no cumple con los parametros")
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
    print(tabulate(tablapago, headers="keys", tablefmt="fancy_grid"))

#Deseamos eliminar información de los pagos ya existentes
def  deletePagos(id):
    data = getIdPago(id)
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

#Deseamos modificar la información de los pagos que ya existen
def ModifyInfoPagos(id):
    data = getCodigoPago(id)
    if(len(data)):
        pago = dict()
        pago["codigo_cliente"] = data["codigo_cliente"]
        while True:
            try:
                if(not pago.get("forma_pago")):
                    formaPago = input("Ingrese la forma de pago: ")
                    if(Procesos.ValidacionDeNombre(formaPago) is not None):
                        pago["forma_pago"] = formaPago
                    else:
                        raise Exception("La forma de pago no cumple con lo establecido")  
                    
                if(not pago.get("id_transaccion")):
                    idTransaccion = input("Ingrese la id de la transaccion: ")
                    if(Procesos.Validaciondetransacciones(idTransaccion) is not None):
                        pago["id_transaccion"] = idTransaccion
                    else:
                        raise Exception("La id de la transaccion no cumple con lo establecido")
                    
                if(not pago.get("fecha_pago")):
                    fechaPago = input("Ingrese la fecha de pago: ")
                    if(Procesos.ValidacionDeFecha(fechaPago) is not None):
                        pago["fecha_pago"] = fechaPago
                    else:
                        raise Exception("La fehca no cumple con lo establecido") 

                if(not pago.get("total")):
                    total = input("Ingrese el total del pago: ")
                    if(Procesos.validacionDeNumerosC(total) is not None):
                        total = int(total)
                        pago["total"] = total
                        break
                    else:
                        raise Exception("El pago no cumple con lo establecido")   
                    
            except Exception as error:
                print(error)
        
        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", headers=headers, data=json.dumps(pago))
        res = peticion.json()
        return [res]
    else:
        return[{
            "messege": "Pago no encontrado",
            "id": id
        }]






def menu():
    while True:
        os.system("clear")
        print("""



    ___       __          _       _      __                 __                  __                       ___     __          
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /__     ____  ___  ____/ (_)___/ /___  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / __ \/ _ \/ __  / / __  / __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /_/ /  __/ /_/ / / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\___/  / .___/\___/\__,_/_/\__,_/\____/____/  
                                                                                     /_/                                     

     
              1. Agregar información de un cliente nuevo
              2. Eliminar información de un cliente
              3. Modificar información del cliente

            Si desea volver, precione: 0
          
""")
        opcion = (input("\nSeleccione una de las opciones: "))
        if re.match(r'^[0-3]+$', opcion) is not None:
            opcion = int(opcion)
            if  opcion == 1:
                print(tabulate(AddInfoPagos()))
                input("Si desea volver, presione: 0")
            elif opcion == 2:
                id = int(input("Por favor, introduzca el id a eliminar: "))
                print(tabulate(deletePagos(id)))
                input("Si desea volver, presione: 0")
            elif opcion == 3:
                print(tabulate(ModifyInfoPagos()))
                input("Si desea volver, presione: 0")
            elif opcion == 0:
                break
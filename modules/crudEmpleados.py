import json
import os
import re
import requests
from tabulate import tabulate
#Servidor de Empleados
def getAllDataEmpleados():
    peticion = requests.get("http://192.168.80.16:5002")
    data = peticion.json()
    return data

#Agregamos un nuevo id cada que agregamos un nuevo Empleado
def nuevoCodigoEmpleado():
    codigoDelEmpleado = list()
    for val in getAllDataEmpleados():
        codigoEmpleado = val.get("codigo_empleado")
        if codigoEmpleado is not None:
            codigoDelEmpleado.append(codigoEmpleado)
    if codigoDelEmpleado:
        return max(codigoDelEmpleado) + 1
    else:
        return 1
    

#Adquirimos el número de id por el codigo
def getCodigoEmplaedo(id):
    peticion = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
    return [peticion.json()] if peticion.ok else[]


def postEmpleados():
    while True:
        print("Hola mundo")
       
def deleteEmpleado(id):
    data = getCodigoEmplaedo(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
        if peticion.status_code == 204:
            data.append({"message" : "El producto fue eliminado correctamente"})
            return{
                "body": data,
                "status" : peticion.status_code
            }
        else:
            return[{
                "body": {
                    "message" : "Producto no encontrado",
                    "data" : id
                },
                "status" : 400
                # Bad request 
                }]






def menu():
    while True:
        os.system("cls")
        print("""
               
    __  ___             __         __        ______                __               __          
   /  |/  /__  ____  __/_/_   ____/ /__     / ____/___ ___  ____  / /__  ____ _____/ /___  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                        /_/                                     
             

               0. Volver atrás.
               1. Agregar información de un Empleado nuevo
               2. Eliminar información de un Empleado ya existente
               3. Modificar información de un Empleado ya existente

               """)
        opcion = (input("\nSeleccione una de las opciones: "))
        if re.match(r'^[0-3]+$', opcion) is not None:
            opcion = int(opcion)
            if  opcion == 1:
                print(tabulate(postEmpleados()))
                input("Si desea volver, presione: 0")
                
            elif opcion == 2:
                id = int(input("Por favor, introduzca el id a eliminar: "))
                print(tabulate(deleteEmpleado(id)))
                input("Si desea volver, presione: 0")
            elif opcion == 3:
                input("Si desea volver, presione: 0")
                print("Que hubo")
            elif opcion == 0:
                break
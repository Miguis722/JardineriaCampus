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
    empleado ={}
    while True:
        try:
            if not empleado.get("codigo_empleado"):
                
                codigo = input("Ingrese el codigo del empleado: ")
                if(re.match(r'^[0-9]+$', codigo) is not None):
                    datas = getCodigoEmplaedo(codigo)
                    if datas:
                        print(tabulate(datas, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("el codigo del empleado ya existe")
                    else:
                        codigo = int(codigo)
                        empleado["codigo_empleado"] = codigo
                else: 
                    raise Exception("El codigo  del producto no cumple con los parametros preesta")
            if not empleado.get("nombre"):
                
                nombre = input("Ingrese el nombre del empleado: ")
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", nombre) is not None):
                    empleado["nombre"] = nombre
                else:
                    raise Exception ("El nombre del empleado no cumple con los parametros preestablecidos")
            if not empleado.get("apellido1"):
                
                apellido_1= input("Ingrese el apellido 1 del empleado: ")
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", apellido_1) is not None):
                    empleado["apellido1"] = apellido_1
                else:
                    raise Exception ("El apellido del empleado proporcionado no cumple con los parametros preestablecidos.")
            if not empleado.get("apellido2"):
                
                apellido_2 = input("Ingrese el apellido 2 del empleado: ")
                if(re.match(r"^[A-Z][a-záéíóúñ]+(?:\s+[A-Z][a-záéíóúñ]+)*$", apellido_2) is not None):
                    empleado["apellido2"] = apellido_2
                else:
                    raise Exception ("El apellido del empleado no cumple con los parametros preestablecidos.")
            if not empleado.get("extension"):
                
                extension = input("Ingrese la extension del empleado: ")
                if(re.match(r"^[0-9\s-]+$", extension) is not None):
                    empleado["extension"] = extension
                else:
                    raise Exception ("La extension del contacto del cliente no cumple con los parametros preestablecidos.")
            if not empleado.get("email"):
                email = input("Ingrese el correo del empleado: ")
                empleado["email"] = email
            if not empleado.get("codigo_oficina"):
                codigo_oficina = input("Ingrese el codigo de la oficina del empleado: ")
                if(re.match(r"^[A-Z-]+$", codigo_oficina) is not None):
                    empleado["codigo_oficina"] = codigo_oficina
                else:
                    raise Exception ("El codigo de oficina del empleado no cumple con los parametros preestablecidos.")
            if not empleado.get("codigo_jefe"):
                codigo_jefe = input("Ingrese el codigo del jefe: ")
                if(re.match(r"^[0-9]+$", codigo_jefe) is not None):
                    empleado["codigo_jefe"] = codigo_jefe
                else:
                    raise Exception ("El codigo del jefe del empleado no cumple con los parametros preestablecidos. ")
            if not empleado.get("puesto"):
                puesto = input("Ingrese el puesto del empleado: ")
                if(re.match(r"^[A-Z][a-zA-Z\s]+$", puesto) is not None):
                    empleado["puesto"] = puesto
                    break
                else:
                    raise Exception ("El puesto del empleado no cumple con los parametros preestablecidos.")
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5003/empleados",  headers=headers , data=json.dumps(empleado, indent=4))
    res = peticion.json()
    tablaEmpleado = [empleado]
    print(tabulate(tablaEmpleado, headers="keys", tablefmt="rounded_grid"))
       
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
                
            elif opcion == 0:
                break
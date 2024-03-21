import json
import os
import re
import requests
from tabulate import tabulate
import Procesosdetextos as Procesos

#Servidor de Oficina
def getAllDataOficina():
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data

#Obtenemos el codigo de la oficina
def getAllCodigoOficina():
    CodigoOficina = list()
    for val in getAllDataOficina():
        CodigoOficina.append(val.get("codigo_oficina"))
    return CodigoOficina



#Deseamos agregar información de una nueva oficina
def postOficina():
    oficina ={}
    while True:
        try:
            if not oficina.get("codigo_oficina"):
                
                cod_oficina = input("Ingrese el codigo de la oficina: ")
                if(re.match(r"^[A-Z-]+$", cod_oficina) is not None):
                    datas = getAllCodigoOficina(cod_oficina)
                    if datas:
                        print(tabulate(datas, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("el codigo de la oficina ya existe")
                    else:
                        codigo_oficina = input("el codigo de la oficina: ")
                        if (re.match(r"^[A-Z-]+$", codigo_oficina) is not None):
                            oficina["codigo_oficina"] = codigo_oficina
                else: 
                    raise Exception("el codigo  de la oficina no cumple con el estandar establecido")
            if not oficina.get("ciudad"):
                
                ciudad = input("Ingrese la ciudad de la oficina: ")
                if(re.match(r"^[A-Z][a-zA-Z]+$", ciudad) is not None):
                    ciudad["ciudad"] = ciudad
                else:
                    raise Exception ("la ciudad de la oficina no cumple con los parametros")
            if not oficina.get("pais"):
                
                pais = input("Ingrese el pais de la oficina ")
                if(re.match(r"^[A-Z][a-zA-Z]+$", pais) is not None):
                    oficina["pais"] = pais
                else:
                    raise Exception ("el pais de la oficina no cumple con los parametros")
            if not oficina.get("region"):
                
                region = input("Ingrese la region de la oficina ")
                if(re.match(r"^[A-Z][a-zA-Z]+$", region) is not None):
                    oficina["region"] = region
                else:
                    raise Exception ("la region de la oficina no cumple con los parametros")
            if not oficina.get("codigo_postal"):
                
                codigo_postal = input("Ingrese el codigo postal de la oficina ")
                if(re.match(r"^[0-9]+$", codigo_postal) is not None):
                    oficina["codigo_postal"] = codigo_postal
                else:
                    raise Exception ("el telefono de contacto del cliente no cumple con los parametros")
            if not oficina.get("telefono"):
                
                telefono = input("Ingrese el telefono de la oficina ")
                if(re.match(r"^[0-9\s-]+$", telefono) is not None):
                    oficina["telefono"] = telefono
                else:
                    raise Exception ("el telefono de la oficina no cumple con los parametros")
            if not oficina.get("linea_direccion1"):
                linea_direccion1 = input("Ingrese la direccion 1 del cliente: ")
                oficina["linea_direccion1"] = linea_direccion1
            if not oficina.get("linea_direccion2"):
                linea_direccion2 = input("Ingrese la direccion 2 del cliente: ")
                oficina["linea_direccion2"] = linea_direccion2
                break
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5005/oficinas",  headers=headers , data=json.dumps(oficina, indent=4))
    res = peticion.json()
    tablaOficina = [oficina]
    print(tabulate(tablaOficina, headers="keys", tablefmt="fancy_grid"))


#Deseamos borrar una oficina ya existente
def deleteOficina(id):
    data = getAllCodigoOficina(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
        if peticion.status_code == 204:
            data.append({"message" : "la oficina fue eliminada correctamente"})
            return{
                "body": data,
                "status" : peticion.status_code
            }
        else:
            return[{
                "body": {
                    "message" : "oficina no encontrada",
                    "data" : id
                },
                "status" : 400
}]

#Deseamos actualizar una oficina ya existente
def updateOficina(id):
    data = getAllCodigoOficina(id)
    if (len(data)):
        oficina = dict()
        while True:
            try:
                if(not oficina.get("codigo_oficina")):
                    codigo = input("Ingrese el codigo de la oficina (Ej: BCN-ES): ")
                    if(Procesos.validacionCoidgoOficina(codigo) is not None):
                        data = getAllCodigoOficina(codigo)
                        if(data):
                            print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                            raise Exception("El codigo oficina ya existe")
                        else:
                            oficina["codigo_oficina"] = codigo
                    else:
                        raise Exception("El codigo oficina no cumple con el estandar establecido")
                    
                if(not oficina.get("ciudad")):
                    ciudad = input("Ingrese la ciudad: ")
                    if(Procesos.ValidacionDeNombre(ciudad) is not None):
                        oficina["ciudad"] = ciudad
                    else:
                        raise Exception("El nombre de la ciudad no cumple con lo establecido")
                
                if(not oficina.get("pais")):
                    pais = input("Ingrese el pais: ")
                    if(Procesos.ValidacionDeNombre(pais) is not None):
                        oficina["pais"] = pais
                    else:
                        raise Exception("El nombre del pais no cumple con lo establecido")
                    
                if(not oficina.get("region")):
                    region = input("Ingrese la region: ")
                    if(Procesos.ValidacionDeNombre(region) is not None):
                        oficina["region"] = region
                    else:
                        raise Exception("El nombre de la region no cumple con lo establecido")
                    
                if(not oficina.get("codigo_postal")):
                    codigoPostal = input("Ingrese el codigo postal: ")
                    if(Procesos.ValidacionDeNumeros(codigoPostal) is not None):
                        oficina["codigo_postal"] = codigoPostal
                    else:
                        raise Exception("El codigo postal no cumple con lo establecido")
                    
                if(not oficina.get("telefono")):
                    telefono = input("Ingrese el numero de telefono: ")
                    if(Procesos.ValidacionNumero(telefono) is not None):
                        oficina["telefono"] = telefono
                    else:
                        raise Exception("El telefono ingresado no cumple con lo establecido")
                    
                if(not oficina.get("linea_direccion1")):
                    direccion1 = input("Ingrese una linea de direccion: ")
                    oficina["linea_direccion1"] = direccion1
                     
                direccion2 = input("Ingrese otra linea de direccion(opcional): ")
                if direccion2:
                    oficina["linea_direccion2"] = direccion2
            except Exception as error:
                print(error)
                continue
            break

        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://154.38.171.54:5005/oficinas/{id}", headers=headers, data=json.dumps(oficina))
        res = peticion.json()
        res["Mensaje"] = "Oficina Actualizada"
        return [res]
    
    else:
        return [{
                    "message": "Oficina no encontrada",
                    "id": id
            }]   

def menu():
    print("""
          

    __  ___             __         __              _____      _            
   /  |/  /__  ____  __/_/_   ____/ /__     ____  / __(_)____(_)___  ____ _
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ / 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/  
                                                                           

          0. Salir del programa.
          1. Guardar una oficina.
          2. Eliminar una oficina.
          3. Actualizar una oficina.


""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if re.match(r'^[0-3]+$', opcion) is not None:
            opcion = int(opcion)
    if(opcion == 1):
        print(tabulate(postOficina()))
    elif(opcion ==2):
        id = int(input("Por favor, introduzca el id a eliminar: "))
        print(tabulate(deleteOficina(id)))
    elif(opcion == 3):
        print("Hola Mundo!")
    elif(opcion == 0):
        exit()
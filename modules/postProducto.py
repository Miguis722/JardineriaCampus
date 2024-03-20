import json
import os
from tabulate import tabulate
import requests
import modules.getGamas as gG
import re
import modules.getProducto as gP

def postProducto():
    #producto = dict()
    #while True:
      #  try:
     #       if(not producto.get("codigo_producto")):
    #            codigo = input("Ingrese el codigo del producto: ")
   #             if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
  #                  data =
    producto = {
        "codigo_producto":input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Selecione la gaa:\n"+"".join([f"\t{i}.{val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    
        }
    #json-server storage/producto.json -b 5002
   
   # Metodo 2
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5008/productos", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

    # Metodo 1
    # peticion = requests.post("http://154.38.171.54:5008/productos", data=json.dumps(producto, indent = 4).encode(("UTF-8")))
    # res = peticion.json()
    # res["Mensaje"] = "Producto Guardado"
    # return [res]

#Primera forma de eliminar  un dato (Metodo profesor: 1)
#def DeleteProducto(id):
 #   peticion = requests.delete(f"http://{id}")
  #  if(peticion.status_code ==204):
   #     return [{
    #        "body":{
     #           "message": "producto eliminado correctamente",
      #          "id": id
       #     }
        #}]
    
#Segunda forma de eliminar un dato (Metodo profesor: 2)
def deleteProducto(id):
    data = gP.getProductCodigo(id)
    if (len(data)):
        peticion = requests.delete(f"http://172.16.102.108:5501/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
        else:
            return {
                "body": [{
                    "message": "Producto no encontrado",
                    "id": id
                }],
                "status": 400,
            }

    
def menu():
    print("""


    ____  _                            _     __               __                          __         __                         __                          __           __            
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __/_/_   ____/ /__     ____  ____  _____/ /_   ____  _________  ____/ /_  _______/ /_____  _____
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ __ \/ ___/ __/  / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /_/ (__  ) /_   / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/\____/____/\__/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                                                                          /_/                     /_/                                                  


            0. Salir del programa
            1. Guardar un producto
            2. Eliminar un producto
            3. Hola mundo
          
          
          """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postProducto()))
    elif(opcion ==2):
        id = int(input("Por favor, introduzca el id a eliminar: "))
        print(tabulate(deleteProducto(id)))
    elif(opcion == 3):
        print("Hola Mundo!")
    elif(opcion == 0):
        exit()
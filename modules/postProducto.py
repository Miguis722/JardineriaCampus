import json
import os
from tabulate import tabulate
import requests
import modules.getGamas as gG
import re

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
   
    peticion = requests.post("             ", data=json.dumps(producto, indent = 4).encode(("UTF-8")))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]


def DeleteProducto(id):
    peticion = requests.delete(f"http://{id}")
    if(peticion.status_code ==204):
        return [{
            "body":{
                "message": "producto eliminado correctamente",
                "id": id
            }
        }]
    
def menu():
    print("""


    ____  _                            _     __               __                          __         __                         __                          __           __            
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __/_/_   ____/ /__     ____  ____  _____/ /_   ____  _________  ____/ /_  _______/ /_____  _____
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ __ \/ ___/ __/  / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /_/ (__  ) /_   / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/\____/____/\__/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                                                                          /_/                     /_/                                                  

            1. Guardar  Productos
            2. Salir del programa
            3.
          
          
          """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postProducto()))
    elif(opcion == 2):
        exit()
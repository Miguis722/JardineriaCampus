import json
import os
from tabulate import tabulate
import requests
import modules.getGamas as gG

def postProducto():
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

import os
from tabulate  import tabulate
import requests

def getAllData():
    peticion = requests.get("http://172.16.106.112:5001")
    data = peticion.json()
    return data

#Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales
#Y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta,
#mostrando en primer lugar los de mayor precio.

#Forma del profesor Miguel
def getAllPriceGama(gama, stock=None):
    condiciones = []
    for val in getAllData:
        if(val.get("gama")== gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse = True)
    for i, val in enumerate(condiciones): 
            condiciones[i] = {
   "codigo": val.get("codigo_producto"),
   "venta": val.get("precio_venta"),
   "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
   "stock": val.get("cantidad_en_stock"),
   "base": val.get("precio_proovedor")
 }
    return condiciones



#Mi forma
def getAllStocksPriceGama(gama):
    StocksPriceGama = []
    for val in getAllData:
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= 100):
                StocksPriceGama.append({
                "Codigo": val.get("codigo_producto"),
                "Nombre": val.get("nombre"),
                "Gama": val.get("gama"),
                "Proveedor": val.get("proveedor"),
                "Descripcion": val.get("descripcion"),
                "Precio": val.get("precio_venta"),
                "Dimensiones": val.get("dimensiones")
                
            })
                StocksPriceGama.sort(key=lambda x: x['Precio'], reverse=True)
                #Aqui lo que estamos haciendo con el 'Precio' es que ordene de mayor a menor la ventana de precios.
                #Lambda se utiliza para crear funciones anónimas, es decir, funciones que no tienen un nombre específico asociado.
    return StocksPriceGama #La función SORT sirve para que ordene algo en orden, sin modificarlo.


#Generamos una función capaz de darnos TODA, la información acerca de un producto por medio de sus codigos de identificación
def  getAllInfoProducto(codigo):
    InfoProducto = []
    for val in getAllData:
          if(val.get("codigo_producto") == codigo):
               InfoProducto.append({
                    "Nombre": val.get("nombre"),
                    "Descripción": val.get( "descripcion" ),
                    "Proovedor": val.get("proveedor"),
                    "Precio Venta": (f"""${"precio_venta"}"""),
                    "Cantidad disponible o en Stock": val.get("cantidad_en_stock")
               })
               InfoProducto.append(codigo)
    return InfoProducto

          


def menu():
    os.system("clear")
    print("""
          
    
    ____                        __              __        ____                 __           __            
   / __ \___  ____  ____  _____/ /____     ____/ /__     / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                                                             

                    1. Listar Productos Ornamentales con Stock Mayor o Igual a 100 (Metodo del profesor Miguel
                    2. Listar Productos Ornamentales con Stock Mayor o Igual a 100 (Mi metodo)
                    3. Buscar un producto por su código
                    Si desea volver, precione la tecla: Esc
        
          
          """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        gama = (input("Ingrese la gama (gama, stock): "))
        print(tabulate(getAllPriceGama(gama), headers= "keys", tablefmt="rounded_grid"))
    elif(opcion == 2):
         gama = str(input("Ingrese la gama: "))
         print(tabulate(getAllStocksPriceGama(gama), headers= "keys", tablefmt="rounded_grid"))
    elif(opcion == 3):
         codigo = (input("Ingrese el código del producto: "))
         print(tabulate(getAllInfoProducto(codigo), headers= "keys", tablefmt="rounded_grid"))
from tabulate  import tabulate
import Storage.producto as pr

#Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales
#Y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta,
#mostrando en primer lugar los de mayor precio.

#Forma del profesor Miguel
#def getAllPriceGama(gama, stock):
    #def gamaStock(val):
        #if(val.get("gama") == gama):
            #return val.get("precio_venta")
    #return pr.producto.sort(key=gamaStock)

#Mi forma
def getAllStocksPriceGama(gama):
    StocksPriceGama = []
    for val in pr.producto:
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= 100):
                StocksPriceGama.append({
                "Gama": val.get("gama"),
                "Codigo": val.get("codigo_producto"),
                "Proveedor": val.get("proveedor"),
                "Precio": val.get("precio_venta")
            })
                StocksPriceGama.sort(key=lambda x: x['Precio'], reverse=True)
                #Aqui lo que estamos haciendo con el 'Precio' es que ordene de mayor a menor la ventana de precios.
                #Lambda se utiliza para crear funciones anónimas, es decir, funciones que no tienen un nombre específico asociado.
    return StocksPriceGama #La función SORT sirve para que ordene algo en orden, sin modificarlo.

def menu():
    print("""
          
    
    ____                        __              __        ____                 __           __            
   / __ \___  ____  ____  _____/ /____     ____/ /__     / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                                                             

                    1. Listar Productos Ornamentales con Stock Mayor o Igual a 100
        
          
          """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        gama = (input("Ingrese la gama: "))
        print(tabulate(getAllStocksPriceGama(gama), headers= "keys", tablefmt="rounded_grid"))
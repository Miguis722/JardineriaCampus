import requests
import os
import re
import requests
from tabulate import tabulate

#Servidor de pagos
def getAllDataPagos():
	peticion = requests.get("http://172.16.106.112:5004")
	data= peticion.json()
	return data

#Devuelve un listado con todos los pagos que se realizaron en el año 2008 mediante Paypal.
#Ordene el resultado de mayor a menor.

def getAllPagosConPayPalEnEl2008():
    PagosPayPal2008 = []
    for pago in pago.pago:
        if  "2008" in  str(pago.fecha): #Comprobamos si la fecha del pago contiene al menos una vez el año 2008
            PagosPayPal2008 =  [x for x in PagosPayPal2008 if x["Fecha"] <= pago["Fecha"]] + [pago]
            
            # Ordenar la lista por las fechas, si son iguales mantener la posicion original del elemento
            PagosPayPal2008.sort(key=lambda x: (x['Fecha'], PagosPayPal2008.index(x)))
    
    return [pagos for pagos in PagosPayPal2008 if "2008" in pagos["Fecha"]]


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

                0. Volver atrás
                1.  Obtener toda la información de los pagos realizados en el 2008 por Paypal

""")
          opcion = (input("\nSeleccione una de las opciones: "))
          if re.match(r'^[0-1]+$', opcion) is not None:
            opcion = int(opcion)
            if  opcion == 1:
                print(tabulate(getAllPagosConPayPalEnEl2008(), headers= "keys", tablefmt="rounded_grid"))
                input("Si desea volver, presione: 0")
            elif opcion == 0:
                break
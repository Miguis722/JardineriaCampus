import requests

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



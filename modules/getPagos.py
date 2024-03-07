import Storage.pago as pago

#Devuelve un listado con todos los pagos que se realizaron en el año 2008 mediante Paypal.
#Ordene el resultado de mayor a menor.

def getAllPagosConPayPalEnEl2008():
    PagosPayPal2008 = []
    for pago in pago.pago:
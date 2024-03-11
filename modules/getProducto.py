from tabulate  import tabulate
import Storage.producto as pr

#Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales
#Y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta,
#mostrando en primer lugar los de mayor precio.

#def getAllPriceGama(gama, stock):
    #def gamaStock(val):
        #if(val.get("gama") == gama):
            #return val.get("precio_venta")
    #return pr.producto.sort(key=gamaStock)


def defAllStocksPriceGama(gama):
    StocksPriceGama = []
    for val in pr.producto:
        if(val.get("Ornamental") == gama):
            if (val.get("cantidad_en_stock")  >= 100):
                gama.append({
                "Gama": val.get("gama"),
                "Codigo": val.get("codigo_producto"),
                "Proveedor": val.get("proveedor"),
            })
                StocksPriceGama.sort(key=StocksPriceGama)
    return gama #La función SORT sirve para que ordene algo en orden, sin modificarlo.
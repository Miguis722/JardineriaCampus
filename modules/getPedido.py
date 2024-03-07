import Storage.pedido as ped

def getAllProcesoPedido():
    ProcesoPedidos = []
    for val in ped.pedido:
        ProcesoPedidos.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado": val.get('estado')
        })
    return ProcesoPedidos

#Devuelve un listado con el codigo de pedido,
#Código de cliente, fecha esperada y fecha de
#Entrega de los pedidos que no han sido entregados.

#date_1 = '2006-01-17'
#date_2 = '2006-01-17'
#start = datetime.strptime(date_1, "%d/%m/%Y")
#end = datetime.strptime(date_2, "%d/%m/%Y")
#diff = end.date() - start.date()
#print(diff.days)

#lista = "/".join(date_1.split("-")[::-1])
#print(lista)
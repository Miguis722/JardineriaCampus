import Storage.pedido as ped
from datetime import datetime

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

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregados = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entregada") is None:
            val["fecha_entregada"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.gate()
        if(diff.gays < 0):
            pedidosEntregados.append({
            "codigo_de_pedido": val.get("codigo_pedido"),
            "codigo_de_cliente": val.get("codigo_cliente"),
            "fecha_esperada": val.get("fecha_esperada"),
            "fecha_entrega": val.get("fecha_entrega")
        })
    return pedidosEntregados
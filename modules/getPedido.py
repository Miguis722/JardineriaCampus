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
        if val.get("estado") == "Entregado":
            fecha_entrega = val.get("fecha_entrega")
            fecha_esperada = val.get("fecha_esperada")
            if fecha_entrega is not None and fecha_esperada is not None:
                date_1 = "/".join(fecha_entrega.split("-")[::-1])
                date_2 = "/".join(fecha_esperada.split("-")[::-1])
                start = datetime.strptime(date_1, "%d/%m/%Y")
                end = datetime.strptime(date_2, "%d/%m/%Y")
                diff = end.date() - start.date()
                if diff.days < 0:
                    pedidosEntregados.append({
                        "codigo_de_pedido": val.get("codigo_pedido"),
                        "codigo_de_cliente": val.get("codigo_cliente"),
                        "fecha_esperada": fecha_esperada,
                        "fecha_entrega": fecha_entrega
                    })
    return pedidosEntregados

#Devuelve un listado con el código de pedido, código de cliente, fecha esperada
#Y fecha de entrega de los pedidos cuya fecha de entrega ha sido al menos dos días antes de la fecha esperada.

def getAllCodigosPedidosClientesFechaEsperadaDODIAS():
    codigosPedidosClientesFechaEsperadaDODIAS = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado":
            codigo_pedido = val.get("codigo_pedido")
            codigo_cliente = val.get("codigo_cliente")
            fecha_esperada = val.get("fecha_esperada")
            fecha_entrega = val.get("fecha_entrega")
            if fecha_entrega is not None and fecha_esperada is not None:  # Verificar que ambas fechas no sean None
                date_1 = "/".join(fecha_entrega.split("-")[::-1])
                date_2 = "/".join(fecha_esperada.split("-")[::-1])
                start = datetime.strptime(date_1, "%d/%m/%Y")
                end = datetime.strptime(date_2, "%d/%m/%Y")
                diff = end.date() - start.date()
                if diff.days == 2:  # Si la diferencia es de 2 días (dos días antes de lo esperado)
                    codigosPedidosClientesFechaEsperadaDODIAS.append({
                        "codigo_de_pedido": codigo_pedido,
                        "codigo_de_cliente": codigo_cliente,
                        "fecha_esperada": fecha_esperada,
                        "fecha_entrega": fecha_entrega
                    })
    return codigosPedidosClientesFechaEsperadaDODIAS

#Devuelve un listado de todos los pedidos que fueron rechazados en 2009
def getAllPedidosRechazados():
    PedidosRechazados = []
    for val in ped.pedido:
        if val.get("estado") =="Rechazado":
            fecha_entrega = val.get("fecha_entrega")
            if fecha_entrega is not None:
                year = fecha_entrega.split('T')[0].split('-')[0]
                if int(year) == 2009:
                    PedidosRechazados.append(val)
    return PedidosRechazados
#Una vez más CHAT GPT me da literalmente en el mismo codigo, punto por punto y sin embargo a el 
#No le mete ningun error.

#Deuelve un listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año.
def getAllPedidosEntregadosEnEnero():
    PedidosEntregadosEnEnero = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado":
            fecha_entrega = val.get("fecha_entrega")
            if fecha_entrega is not None:
                month = fecha_entrega.split('T')[0].split('-')[1] #Usamos el número 1 al final para que solo le tome importancia a enero
                if month == '01':
                    PedidosEntregadosEnEnero.append(val)
    return PedidosEntregadosEnEnero

#Devuelve un listado con todos los pagos que se realizaron en el año 2008 mediante Paypal.
#Ordene el resultado de mayor a menor.


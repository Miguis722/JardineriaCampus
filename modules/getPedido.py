import os
from tabulate import tabulate
import requests
from datetime import datetime

#Servidor de Pedidos
def getAllDataPedidos():
    peticion = requests.get("http://172.16.106.112:5006")
    data = peticion.json()
    return data



def getAllProcesoPedido():
    ProcesoPedidos = []
    for val in getAllDataPedidos:
        ProcesoPedidos.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado": val.get('estado')
        })
    return ProcesoPedidos

#Devuelve un listado con el codigo de pedido,
#Código de cliente, fecha esperada y fecha de
#Entrega de los pedidos que no han sido entregados.

#Mi metodo más recortado
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    peticion = requests.get("http://")
    data = peticion.json()

#SELECCIONAMOS TODo EL TEXTO Y PRESIONAMOS: CTRL + K + C
    
#Mi metodo
# def getAllPedidosEntregadosAtrasadosDeTiempo():
#     pedidosEntregados = []
    for val in getAllDataPedidos:
         if val.get("estado") == "Entregado":
             fechaEntrega = val.get("fechaEntrega")
             fecha_esperada = val.get("fecha_esperada")
             if fechaEntrega is not None and fecha_esperada is not None:
                 date_1 = "/".join(fechaEntrega.split("-")[::-1])
                 date_2 = "/".join(fecha_esperada.split("-")[::-1])
                 start = datetime.strptime(date_1, "%d/%m/%Y")
                 end = datetime.strptime(date_2, "%d/%m/%Y")
                 diff = end.date() - start.date()
                 if diff.days < 0:
                     pedidosEntregado.append({
                         "codigo_de_pedido": val.get("codigo_pedido"),
                         "codigo_de_cliente": val.get("codigo_cliente"),
                         "fecha_esperada": fecha_esperada,
                         "fechaEntrega": fechaEntrega
                     })
    return pedidosEntregado

#Devuelve un listado con el código de pedido, código de cliente, fecha esperada
#Y fecha de entrega de los pedidos cuya fecha de entrega ha sido al menos dos días antes de la fecha esperada.

def getAllCodigosPedidosClientesFechaEsperadaDODIAS():
    codigosPedidosClientesFechaEsperadaDODIAS = []
    for val in getAllDataPedidos:
        if val.get("estado") == "Entregado":
            codigo_pedido = val.get("codigo_pedido")
            codigo_cliente = val.get("codigo_cliente")
            fecha_esperada = val.get("fecha_esperada")
            fechaEntrega = val.get("fechaEntrega")
            if fechaEntrega is not None and fecha_esperada is not None:  # Verificar que ambas fechas no sean None
                date_1 = "/".join(fechaEntrega.split("-")[::-1])
                date_2 = "/".join(fecha_esperada.split("-")[::-1])
                start = datetime.strptime(date_1, "%d/%m/%Y")
                end = datetime.strptime(date_2, "%d/%m/%Y")
                diff = end.date() - start.date()
                if diff.days == 2:  # Si la diferencia es de 2 días (dos días antes de lo esperado)
                    codigosPedidosClientesFechaEsperadaDODIAS.append({
                        "codigo_de_pedido": codigo_pedido,
                        "codigo_de_cliente": codigo_cliente,
                        "fecha_esperada": fecha_esperada,
                        "fechaEntrega": fechaEntrega
                    })
    return codigosPedidosClientesFechaEsperadaDODIAS

#Devuelve un listado de todos los pedidos que fueron rechazados en 2009
def getAllPedidosRechazados():
    PedidosRechazados = []
    for val in getAllDataPedidos:
        if val.get("estado") =="Rechazado":
            fechaEntrega = val.get("fechaEntrega")
            if fechaEntrega is not None:
                year = fechaEntrega.split('T')[0].split('-')[0]
                if int(year) == 2009:
                    PedidosRechazados.append(val)
    return PedidosRechazados
#Una vez más CHAT GPT me da literalmente en el mismo codigo, punto por punto y sin embargo a el 
#No le mete ningun error.

#Deuelve un listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año.
def getAllPedidosEntregadosEnEnero():
    PedidosEntregadosEnEnero = []
    for val in getAllDataPedidos:
        if val.get("estado") == "Entregado":
            fechaEntrega = val.get("fechaEntrega")
            if fechaEntrega is not None:
                month = fechaEntrega.split('T')[0].split('-')[1] #Usamos el número 1 al final para que solo le tome importancia a enero
                if month == '01':
                    PedidosEntregadosEnEnero.append(val)
    return PedidosEntregadosEnEnero



def menu():
    os.system("clear")
    print("""



 _______                                  _                 __         _______               __  _        __               
|_   __ \                                / |_              |  ]       |_   __ \             |  ](_)      |  ]              
  | |__) |  .---. _ .--.    .--.  _ .--.`| |-'.---.    .--.| | .---.    | |__) |.---.   .--.| | __   .--.| |  .--.  .--.   
  |  __ /  / /__\[ '/'`\ \/ .'`\ [ `/'`\]| | / /__\\ / /'`\' |/ /__\\   |  ___// /__\\/ /'`\' |[  |/ /'`\' |/ .'`\ ( (`\]  
 _| |  \ \_| \__.,| \__/ || \__. || |    | |,| \__., | \__/  || \__.,  _| |_   | \__.,| \__/  | | || \__/  || \__. |`'.'.  
|____| |___|'.__.'| ;.__/  '.__.'[___]   \__/ '.__.'  '.__.;__]'.__.' |_____|   '.__.' '.__.;__|___]'.__.;__]'.__.'[\__) ) 
                 [__|                                                                                                      
         
          
        1. Obtener toda la información de los procesos de los pedidos.
        2. Obtener toda la información de los pedidos entregados fuera de tiempo.
        3. Obtener toda la información de los pedidos entregados dos dias antes de la fecha esperada.
        Si desea volver, precione la tecla: Esc
          
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllProcesoPedido(),headers="keys", tablefmt="rounded_grid"))
    if(opcion == 2):
        print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(),headers="keys",tablefmt="rounded_grid"))
    if(opcion == 3):
        print(tabulate(getAllCodigosPedidosClientesFechaEsperadaDODIAS(), headers="keys", tablefmt="rounded_grid"))

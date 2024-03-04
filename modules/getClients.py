import Storage.cliente as cli

def search():
    clienteNames = list()
    for val in cli.clientes:
    #No es necesario poner indice y enumerate
        clienteNames.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')})
    return clienteNames
#Estamos pidiendo solamente los nombres de las personas

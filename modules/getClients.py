import Storage.cliente as cli

def search():
    clienteNames = list()
    for i,val in enumerate(cli.clientes):
        clienteNames.append(val.get('nombre_cliente'))
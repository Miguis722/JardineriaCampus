import Storage.cliente as cli

def search():
    clienteNames = list()
    for val in cli.clientes:
    #No es necesario poner indice y enumerate
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
        clienteNames.append(codigoName)
    return clienteNames
#Estamos pidiendo solamente los nombres de las personas

def getOneClienteCodigo(codigo):
    for val in cli.clientes:  
        if(val.get('codigo_cliente') == codigo):
            return{
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            }
#Aqui haremos que solo nos de un nombre por codigo

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(val)
    return clienteCredic
#Filtro que nos cuele solamente el limite crediticio y la ciudad especifica.

def getAllClientePaisRegionCiudad(pais,region, ciudad):
    clientZone = list()
    for val in cli.clientes:
        if(
            val.get('pais') == pais and
            (val.get('region')== region or val.get('region') == None) and
            (val.get('ciudad')== ciudad or val.get('ciudad') == None)
            ):
            
            clientZone.append(val)
            
    return clientZone

            
            
import modules.getClients as logic

logic.cli.clientes.append({"nombre": "prueba"})
print(logic.cli.clientes)
#Podemos observar que EFECTIVAMENTE, lo agrego a cliente
#Pero no donde queremos, sino que lo guardo en el archivo CACHÉ

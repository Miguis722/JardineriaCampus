import modules.getClients as cliente
import modules.getOficina as oficina


print(cliente.getAllClientePaisRegionCiudad("France", None, "Paris" ))
#Estamos pidiendo que se nos muestre el pais, la region y la ciudad de todos en general SIN ningúna condición.



#print(cliente.getAllClientCreditCiudad(5000, "Humanes"))
#Estamos pidiendo que si la persona pasa del limite crediticio y
#Su ciudad sea igual a la que se este buscando se nos muestre.


#print(cliente.search())
#Estamos pidiendo solamente los nombres de las personas


#logic.cli.clientes.append({"nombre": "prueba"})
#print(logic.cli.clientes)
    #Podemos observar que EFECTIVAMENTE, lo agrego a cliente
    #Pero no donde queremos, sino que lo guardo en el archivo CACHÉ

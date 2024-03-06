from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado



print(tabulate(empleado.getAllPuestosNombreApellidoEmail(7),tablefmt="grid"))
#Estamos pidiendo que se nos muestre el nombre, los apellidos, el email y el nombre del puesto en el que se encuentra el jefe.


#print(tabulate(empleado.getAllNombreApellidoEmailJefe(7), tablefmt="grid"))
#Estamos pidiendo que se nos muestren todos los Emails de los jefes que tengan el codigo especifico que se pide



#print(tabulate(oficina.getAllCiudadTelefono("España"), tablefmt="grid"))
#Esta pidiendo que se nos muestre todas las oficinas que se encuentren en España.

#print(cliente.getAllClientePaisRegionCiudad("France", None, "Paris" ))
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

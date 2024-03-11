import sys
import msvcrt #Modulo para leer teclas sin bloqueo en windows
from tabulate import tabulate

import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as Pedidos
import modules.getPagos as Pagos

#Lista para almacenar el historial de menús
historial_menu = []

def procesar_tecla():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b': #Verificar si la tecla presionada es ESC
                return "atras"
            else:
                return key.decode('utf-8')

#En este caso, queremos hacer un menú que haga la recopilación de todos los filtros para que se escojan

#def menu():
    #https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
    #Está pagina web sirve para sacar el arte ASCII
    

# En este caso, queremos hacer un menú que haga la recopilación de todos los filtros para que se escojan
def menu():
        print("""
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                

                    1. Cliente
                    2. Oficina
                    3. Empleado
                    4. Pedidos
    """)

        opcion = int(input("\nSeleccione una de las : "))
        if opcion == 1:
                cliente.menu()
                historial_menu.append(menu)
        elif opcion == 2:
                oficina.menu()
                historial_menu.append(menu)
        elif opcion == 3:
                empleado.menu()
                historial_menu.append(menu)
        elif opcion == 4:
                Pedidos.menu()
                historial_menu.append(menu)

        # Definimos función para regresar al menú anterior
        def regresar_menu():
            if historial_menu:
                menu_anterior = historial_menu.pop()  # Obtener el menú anterior del historial
                print("Regresando al menú anterior...")
                menu_anterior()  # Ejecutar el menú anterior
            else:
                print("No hay menús anteriores.")

        # Hacemos los procesos principales del programa
        while True:
            accion = procesar_tecla()                
            if accion == "atras":
                regresar_menu()
            else:
                menu()
menu()

#def menu():
#    contador = 1
#    print("Menu Principal")
#    for nombre, objeto in sys.modules.items():
#        if nombre.startswith("modules"):
#            modulo_name = getattr(objeto, "__name__", None)
#            if modulo_name and modulo_name != "modules":
#                print(f"{contador}. {modulo_name.split('get')[-1]} ")
#                contador += 1

#menu()


#print(tabulate(Pedidos.getAllPedidosEntregadosEnEnero(), tablefmt= "grid"))
#Estamos pidiendo que se nos muestren todos los pedidos de Enero  entregados.


#print(tabulate(Pedidos.getAllPedidosRechazados(), tablefmt= "grid"))
#Estamos pidiendo que se realice una lista con todos los pedidos que han sido  rechazados

#print(tabulate(Pedidos.getAllCodigosPedidosClientesFechaEsperadaDODIAS(), tablefmt="grid"))
#Estamos pidiendo todos los pedidos que se encuentran entregados, pero que se entregaron DOS dias antes de lo esperado.

#print(tabulate(Pedidos.getAllPedidosEntregadosAtrasadosDeTiempo(), tablefmt="grid"))
#Estamos pidiendo todos los pedidos que se encuentren entregados, pero que se entregaron
#De forma retardada.

#print(tabulate(Pedidos.getAllProcesoPedido(), tablefmt="grid"))
#Estamos pidiendo que se nos muestre el estado de todos los pedidos, si estos fueron
#Ya entregados, pendientes o si fueron rechazados

#print(tabulate(cliente.getAllnombreClientesEspañoles(1), tablefmt="grid"))
#Estamos pidiendo el nombre de todos los clientes Españoles

#print(tabulate(empleado.getAllNombreApellidosPuestosNoREPVENTAS("Representante Ventas"),tablefmt="grid"))
#Estamos pidiendo que se nos muestre el nombre, apellido, y el puesto de los que NO SEAN representantes de ventas.

#print(tabulate(empleado.getAllPuestosNombreApellidoEmail(7),tablefmt="grid"))
#Estamos pidiendo que se nos muestre el nombre, los apellidos, el email y el nombre del puesto en el que se encuentra el jefe.


#print(tabulate(empleado.getAllNombreApellidoEmailJefe(7), tablefmt="grid"))
#Estamos pidiendo que se nos muestren todos los Emails de los jefes que tengan el codigo especifico que se pide


#Importante resaltar que antes de todo (oficina.) o (empleado.) es el lugar de procedencia de la información.
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

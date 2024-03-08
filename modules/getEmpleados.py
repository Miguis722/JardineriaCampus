from tabulate import tabulate
import Storage.empleado as em
#Devuelve un listado con el nombre, apellidos y email
#de los empleados cuyo jefe tiene un código de jefe igual a 7.

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmailJefe = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmailJefe.append(
                {
                    "Nombre": val.get("nombre"),
                    "Apellidos": (f"{val.get('apellido1')} {val.get('apellido2')}"),
                    "Email": val.get("email"),
                    "Director": val.get("codigo_jefe")
                }
            )
    #Aqui estamos pidiendo que SI el codigo que pedimos, es igual a alguno de la base de datos, se realice el proceso de IF, el cual cuando finalice va a 
    #Volver todos los datos al punto anterior al if.
    return nombreApellidoEmailJefe

#Devuelve el nombre del puesto, nombre, apellidos 
# y email del jefe de la empresa.

def getAllPuestosNombreApellidoEmail(codigo):
    puestosNombreApellidoEmail = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            puestosNombreApellidoEmail.append({
                "Nombre": val.get("nombre"),
                "Apellidos": (f"{val.get('apellido1')} {val.get('apellido2')}"),
                "Email": val.get("email"),
                "Nombre del puesto en el que opera": val.get("puesto")
            })
    return puestosNombreApellidoEmail

#Devuelve un listado con el nombre, apellidos y 
#puesto de aquellos empleados que no sean representantes de ventas.

def getAllNombreApellidosPuestosNoREPVENTAS(puesto):
    nombreApellidosPuestosNoREPVENTAS = []
    for val in em.empleados:
        if(val.get("puesto") != puesto):
            nombreApellidosPuestosNoREPVENTAS.append(
                {
                    "Nombre": val.get("nombre"),
                    "Apellidos": (f"{val.get('apellido1')} {val.get('apellido2')}"),
                    "Nombre del puesto en el que opera": val.get("puesto")
                }
            )
    return nombreApellidosPuestosNoREPVENTAS




def menu():
    print("""


______                      _             _                             _                _           
| ___ \                    | |           | |                           | |              | |          
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___    ___ _ __ ___  _ __ | | ___  __ _  __| | ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \  / _ \ '_ ` _ \| '_ \| |/ _ \/ _` |/ _` |/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ |  __/ | | | | | |_) | |  __/ (_| | (_| | (_) \__ \
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___|  \___|_| |_| |_| .__/|_|\___|\__,_|\__,_|\___/|___/
          | |                                                    | |                                 
          |_|                                                    |_|                                 
     
        1. Obtener todos los nombres de los empleados dependiendo del número del jefe.
        2. Obtener nombre del puesto, el nombre del operador y el email del jefe de la empresa
        3. Obtener toda la información de un  empleado por su puesto
          
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        codigo = int(input("Ingrese el codigo de jefe: "))
        print(tabulate(getAllNombreApellidoEmailJefe(codigo),headers="keys", tablefmt="rounded_grid"))
    if(opcion == 2):
        codigo = int(input("Ingrese el codigo del empleado: "))
        print(tabulate(getAllPuestosNombreApellidoEmail(codigo),headers="keys",tablefmt="rounded_grid"))
    if(opcion == 3):
        puesto = int(input("Ingrese el puesto: "))
        print(tabulate(getAllNombreApellidosPuestosNoREPVENTAS(puesto), headers="keys", tablefmt="rounded_grid"))


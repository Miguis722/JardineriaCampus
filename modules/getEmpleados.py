import Storage.empleado as em
#Devuelve un listado con el nombre, apellidos y email
#de los empleados cuyo jefe tiene un código de jefe igual a 7.

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmailJefe = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmailJefe.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": (f"{val.get('apellido1')} {val.get('apellido2')}"),
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
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
                "nombre": val.get("nombre"),
                "apellidos": (f"{val.get('apellido1')} {val.get('apellido2')}"),
                "email": val.get("email"),
                "nombre_puesto": val.get("puesto")
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
                    "nombre": val.get("nombre"),
                    "apellidos": (f"{val.get('apellido1')} {val.get('apellido2')}"),
                    "puesto": val.get("puesto")
                }
            )
    return nombreApellidosPuestosNoREPVENTAS

#Devuelve un listado con el nombre de todos los clientes españoles


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
     
        1. Obtener todos los empleados (codigo y nombre)
        2. Obtener un cliente por el codigo (codigo y nombre)
        3. Obtener toda la información de un cliente según su limite de credito y ciudad que pertenece (ejemplo: 3000.0, San Francisco)
          
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllClienteName(),headers="keys", tablefmt="rounded_grid"))
    if(opcion == 2):
        codigoCliente = int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getOneClienteCodigo(codigoCliente),headers="keys",tablefmt="rounded_grid"))
    if(opcion == 3):
        codigoCliente = int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getAllClientCreditCiudad(codigoCliente), headers="keys", tablefmt="rounded_grid"))
    if(opcion == 4):
        ciudad = input("Ingrese la ciudad del cliente: ")
        print(tabulate(getAllClientCiudad(ciudad), headers="keys", tablefmt="rounded_grid"))
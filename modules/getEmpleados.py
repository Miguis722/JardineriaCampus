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
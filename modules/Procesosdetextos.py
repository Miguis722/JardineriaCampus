import re

def ValidacionDeNumeros(numero):
    val = re.match(r'[0-9]+$', numero)
    return val

def ValidacionDeCodigo(codigo):
    val = re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)
    return val

def ValidacionCodigoDeOficina(codigo):
    val = re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo)
    return val

def ValidacionDeNombre(nombre):
    val = re.match(r'^([A-ZÑ][a-zñ]*\s*)+$', nombre)
    return val

def ValidacionDeDimension(dimensiones):
    val = re.match(r'^\s*[0-9]+\s*-\s*[0-9]+\s*$', dimensiones)
    return val

def validacionDeNumeros(numero):
    val = re.match(r'^\s*\d+(\.\d+)?\s*$', numero)
    return val

def ValidacionNumero(numero):
    val = re.match(r'^\s*(\+\d{1,3}\s*)?\s*(\(\d+\))?\s*\d+(?:[\s-]?\d+)*\s*$', numero)
    return val

def ValidacionDeFecha(fecha):
    val = re.match(r'^\d{4}-\d{2}-\d{2}$', fecha)
    return val

def Validaciondetransacciones(transaccion):
    val = re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', transaccion)
    return val

def ValidacionSiNo(confirmacion):
    val = re.match(r'^[sn]$', confirmacion)
    return val
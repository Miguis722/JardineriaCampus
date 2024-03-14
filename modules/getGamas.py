import requests

#Servidor de Gamas
def getAllDataGamas():
    peticion = requests.get("http://172.16.106.112:5007")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllDataGamas():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
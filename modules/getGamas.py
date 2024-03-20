import requests
import json

#Servidor de Gamas
def getAllDataGamas():
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllDataGamas():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
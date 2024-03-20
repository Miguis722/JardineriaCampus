import requests
import json
import modules.getProducto as gP
#Primera forma de eliminar  un dato (Metodo profesor: 1)
#def DeleteProducto(id):
 #   peticion = requests.delete(f"http://{id}")
  #  if(peticion.status_code ==204):
   #     return [{
    #        "body":{
     #           "message": "producto eliminado correctamente",
      #          "id": id
       #     }
        #}]
    
#Segunda forma de eliminar un dato (Metodo profesor: 2)
def deleteProducto(id):
    data = gP.getProductCodigo(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
        else:
            return {
                "body": [{
                    "message": "Producto no encontrado",
                    "id": id
                }],
                "status": 400,
            }
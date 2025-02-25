#Poder mostrar datos de una firebase con un print
import requests

response = requests.get("https://iot2025-60b40-default-rtdb.firebaseio.com/sensor.json")
print (f"{response.text}")


#https://iot2025-60b40-default-rtdb.firebaseio.com/sensor.json

#Para mandar datos (post)
datos = {"sensor":45}
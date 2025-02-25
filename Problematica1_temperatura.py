from gpiozero import DistanceSensor, Buzzer
from time import sleep

# Configuración de pines
sensor = DistanceSensor(echo=24, trigger=23)
buzzer = Buzzer(18)

# Definir distancia mínima (en cm)
DISTANCIA_MINIMA = 10

def alerta_distancia():
    while True:
        # Obtener la distancia medida por el sensor
        distancia = sensor.distance * 100  # Convertir a cm

        # Imprimir la distancia medida
        print(f"Distancia: {distancia:.2f} cm")

        # Activar el buzzer si la distancia es menor que la mínima
        if distancia < DISTANCIA_MINIMA:
            print("¡Distancia demasiado corta! Activando buzzer...")
            buzzer.on()
        else:
            buzzer.off()

        sleep(0.1)  # Esperar un poco antes de la siguiente medición

# Ejecutar el código
try:
    alerta_distancia()
except KeyboardInterrupt:
    print("Programa terminado.")

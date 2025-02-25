from gpiozero import OutputDevice as Vibration
import time
from gpiozero import Button

#definir el pin de vibracion
vibration_sensor = Vibration(27)
button = Button(26)

#declaracion
try:
    while True:
        if button.is_pressed:
            vibration_sensor()
        else:
            vibration_sensor.off()
except KeyboardInterrupt:
    vibration_sensor.close()

#turn on vibration
#vibration_sensor.on()
#tiempo en segundos
#time.sleep(0.5)
#parar la vibracion


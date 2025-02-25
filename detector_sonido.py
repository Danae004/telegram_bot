from gpiozero import DigitalInputDevice as Sound
import time

#Definicion del pin
sound_sensor = Sound(24)

while True:
    #Muestra el mensaje de sonido detectado o no
    if(sound_sensor.value == 0):
        print('Sound detect')
        time.sleep(0.1)
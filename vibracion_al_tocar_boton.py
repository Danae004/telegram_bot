from gpiozero import OutputDevice as Vibration
import time

#definir el pin de vibracion
vibration_sensor = Vibration(27)

#turn on vibration
vibration_sensor.on()
#tiempo en segundos
time.sleep(0.5)
#parar la vibracion
vibration_sensor.off()
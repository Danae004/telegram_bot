from gpiozero import Buzzer
import time
#Si ponemos el 17 no debe de funcionar.
buzzer = Buzzer(18)


#Make buzzer sound
buzzer.on()
time.sleep(0.5)
#Parar el sonido del buzzer
buzzer.off()

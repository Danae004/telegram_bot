from gpiozero import Button,Buzzer
import time

#Configuracion del boton
button = Button(27)
buzzer = Buzzer(18)
 
try:
    while True:
        if button.is_pressed:
            buzzer.on()
        else:
            buzzer.off()
except KeyboardInterrupt:
    buzzer.closet()
    
                
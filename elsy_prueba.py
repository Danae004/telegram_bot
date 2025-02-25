import time
import csv
import smbus
from DFRobot_DHT20 import DFRobot_DHT20
from gpiozero import Buzzer

# Variables para el sensor DHT20 (Temperatura y Humedad)
I2C_BUS = 0x01  # default use I2C1 bus
I2C_ADDRESS = 0x38  # default I2C device address
dht20 = DFRobot_DHT20(I2C_BUS, I2C_ADDRESS)

# Inicializar sensor DHT20
if not dht20.begin():
    print("DHT20 sensor initialization failed")

# Variables para el sensor de luz
bus = smbus.SMBus(1)

# Inicializar el buzzer (asumiendo que está conectado al pin GPIO 18)
buzzer = Buzzer(18)

class LightSensor():
    def __init__(self):
        self.DEVICE = 0x5c  # Default device I2C address
        self.POWER_DOWN = 0x00
        self.POWER_ON = 0x01
        self.RESET = 0x07
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        self.ONE_TIME_LOW_RES_MODE = 0x23

    def convertToNumber(self, data):
        return ((data[1] + (256 * data[0])) / 1.2)

    def readLight(self):
        data = bus.read_i2c_block_data(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE_1)
        return self.convertToNumber(data)

def save_to_csv(light_level, temperature, humidity, timestamp):
    # Guardar los datos en el archivo CSV
    with open('sensor_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, light_level, temperature, humidity])

def save_alarm_to_csv(temperature, timestamp):
    # Guardar los datos de la alarma en un archivo CSV separado
    with open('alarm_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temperature, "Temperatura alta - Alarma activada"])

def main():
    # Inicializar sensor de luz
    light_sensor = LightSensor()

    # Crear los archivos CSV si no existen y agregar los encabezados
    try:
        with open('sensor_data.csv', mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Light Level (lx)', 'Temperature (°C)', 'Humedad (%)'])
    except FileExistsError:
        pass  # El archivo ya existe, no es necesario crear los encabezados de nuevo

    try:
        with open('alarm_data.csv', mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Temperature (°C)', 'Alarm Message'])
    except FileExistsError:
        pass  # El archivo ya existe, no es necesario crear los encabezados de nuevo

    try:
        while True:
            # Leer los datos del sensor de luz
            light_level = light_sensor.readLight()

            # Leer los datos de temperatura y humedad del DHT20
            T_celcius, humidity, crc_error = dht20.get_temperature_and_humidity()
            if crc_error:
                print("CRC Error, skipping this reading")
                continue  # Si hay error, saltamos este ciclo
            else:
                # Convertir la temperatura a Fahrenheit (opcional)
                T_fahrenheit = T_celcius * 9 / 5 + 32

                # Obtener la marca de tiempo actual
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                # Imprimir los datos en la consola (opcional)
                print(f"Nivel de luz: {light_level} lx, Temperatura: {T_celcius} °C, Humedad: {humidity} %")

                # Verificar si la temperatura es mayor a 16°C
                if T_celcius > 16:
                    print("¡Temperatura alta! Activando alarma...")
                    buzzer.on()  # Activa el buzzer
                    time.sleep(0.5)  # Sonido del buzzer por 0.5 segundos
                    buzzer.off()  # Apaga el buzzer

                    
                    save_alarm_to_csv(T_celcius, timestamp)

                
                save_to_csv(light_level, T_celcius, humidity, timestamp)

            
            time.sleep(2)

    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")

if __name__ == "__main__":
    main()
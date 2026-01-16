# pip install pyserial en cmd si fuera nesecario

import serial
import time

arduino = serial.Serial('COM1', 9600)  # Reemplaza 'COM1' con el puerto correcto
time.sleep(2)  # Espera a que la conexión se establezca 2 milisegundos
while True:
    valor=arduino.readline().strip()  # Lee una línea del Arduino
    print("Lectura Ponteciometro: ",valor.decode('utf-8'))  # Decodifica y muestra el valor leído
arduino.close()  # Cierra la conexión cuando se termine (aunque en este caso nunca se llega aquí)   

    


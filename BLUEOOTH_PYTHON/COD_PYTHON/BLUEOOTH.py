#prende y apaga un LED conectado a un Arduino mediante Python
import serial
import time

arduino=serial.Serial("COM8",38400,timeout=1)
time.sleep(2)

print("Conexión establecida con Arduino")
while True:
    respuesta = input("Encender(e) / Apagar(a) / Salir(q): ").strip().lower()
    if respuesta == "e":
        arduino.write(b"e")
    elif respuesta == "a":
        arduino.write(b"a")
    elif respuesta == "q":
        break

arduino.close()
print("Puerto serial cerrado")
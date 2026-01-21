#prende y apaga un LED conectado a un Arduino mediante Python
import serial
import time

arduino=serial.Serial("COM6",9600)# COM1 PARA USO DEL PROTEUS
time.sleep(2)

print("Conexión establecida con Arduino")
while True:
    respuesta = input("Encender (e) / Apagar (a) / Salir (q): ")
    if respuesta == "e":
        arduino.write(b'e')
    elif respuesta == "a":
        arduino.write(b'a')
    elif respuesta == "q":
        break
        
arduino.close()
print("Puerto serial cerrado")
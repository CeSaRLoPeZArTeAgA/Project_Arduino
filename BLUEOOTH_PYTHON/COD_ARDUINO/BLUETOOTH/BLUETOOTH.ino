/*
  ======================= HELP =======================

  Descripción:
  Este programa permite controlar un LED conectado al
  pin digital 13 de Arduino mediante comandos enviados
  por:
    - El Monitor Serial (USB)
    - Un módulo Bluetooth (SoftwareSerial en pines 10 y 11)

  Configuración:
    - Bluetooth RX  -> Pin 10
    - Bluetooth TX  -> Pin 11
    - LED           -> Pin 13
    - Velocidad USB -> 9600 baudios
    - Velocidad BT  -> 38400 baudios

  Comandos disponibles:
    'e' : Enciende el LED (pin 13 en HIGH)
    'a' : Apaga el LED   (pin 13 en LOW)

  Uso:
    - Enviar los caracteres 'e' o 'a' desde el Monitor Serial
      o desde una aplicación Bluetooth.
    - Los comandos recibidos por USB se muestran en el
      Monitor Serial como confirmación.

  ====================================================
*/

#include <SoftwareSerial.h>

SoftwareSerial miBT(10,11); // RX, TX
const int pin13 = 13;

void setup() {
  Serial.begin(9600);      // USB (PC <-> Arduino)
  Serial.println("Listo Conexion Serial");//impresion en monitor serial

  miBT.begin(38400);       // configuracion de rapidez de BT

  pinMode(pin13, OUTPUT);// apertura del pin digital 13,para manejo de led
}

void procesar(char c){
  if (c == 'e') digitalWrite(pin13, HIGH);
  if (c == 'a') digitalWrite(pin13, LOW);
}

void loop() {

  //lectura a travez de puerto serial
  if (Serial.available() > 0) {
    char c = Serial.read();
    procesar(c);
    Serial.write(c);
    Serial.println("Procesado orden por puerto Serial");
  }

  //lectura a travez de BT
  if (miBT.available() > 0) {
    char c = miBT.read();
    procesar(c);
  }
  
}


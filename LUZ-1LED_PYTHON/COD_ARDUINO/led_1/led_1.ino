//PROGAMA DE MANEJO DE 1 LED

const int pin13=13;//Define una constante llamada pin13 asociada al pin digital 13 del Arduino.
void setup() {
  Serial.begin(9600);//Inicia la comunicación serial a 9600 baudios, lo que permite enviar y recibir datos desde el monitor serial del IDE de Arduino.
  pinMode(pin13,OUTPUT);//Configura el pin 13 como salida, para poder enviarle señales HIGH o LOW.
}

void loop() {
  if(Serial.available()>0){ //verifica si hay datos disponibles en el puerto serial.
    char caracter= Serial.read();//Si hay al menos un byte, se lee un carácter y se guarda en la variable caracter
    if(caracter =='e'){
      digitalWrite(pin13,HIGH);//El pin 13 se pone en alto (5V) → el LED se enciende.
    }
    if(caracter =='a'){
      digitalWrite(pin13,LOW);//El pin 13 se pone en bajo (0V) → el LED se apaga.
    }
  }
}

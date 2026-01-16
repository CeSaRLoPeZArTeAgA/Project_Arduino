const int pinA0=0;
int valor=0;
void setup() {
  Serial.begin(9600);
}

void loop() {
  valor=analogRead(pinA0);
  Serial.println(valor,DEC);
}

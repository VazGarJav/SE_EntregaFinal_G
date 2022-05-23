int pulsador = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(pulsador, INPUT_PULLUP);
  Serial.begin(9600);
}

int valor; 
void loop() {
  // put your main code here, to run repeatedly:
   valor = !digitalRead(pulsador);
   Serial.println(valor);
   delay(100);
}

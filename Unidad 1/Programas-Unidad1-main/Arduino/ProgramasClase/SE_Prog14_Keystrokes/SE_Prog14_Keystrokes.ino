int pulsador = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(pulsador, INPUT_PULLUP);
  Serial.begin(9600);
}
int valor = 0;
void loop() {
  // put your main code here, to run repeatedly:
  valor = digitalRead(pulsador);
  Serial.println(String(valor));
  delay(100);
}

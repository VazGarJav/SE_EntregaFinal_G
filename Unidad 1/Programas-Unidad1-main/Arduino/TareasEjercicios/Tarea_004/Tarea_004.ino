int leds[8] = { 6, 7, 8, 9, 10, 11, 12, 13};
void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);

}
int v, aux; //numero decimal a leer
void loop() {
  v = analogRead(A0);
  aux = map(v, 0, 1023, 0, 7);
  Serial.println("valor leido " + String(aux));
  digitalWrite(leds[aux],1);
  delay(1000);
  limpiar();
}
void limpiar()
{
  for (int i=0; i<8; i++)
  {
    digitalWrite(leds[i],0);
  }
}

int leds[8] = { 6, 7, 8, 9, 10, 11, 12, 13};


void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  randomSeed(analogRead(A0));
}
int v;
void loop() {
  // put your main code here, to run repeatedly:
  limpiar();
  v = random(8);
  digitalWrite(leds[v], 1);
  delay(1000);
}

void limpiar()
{
  for (int i = 0; i < 8; i++)
  {
    digitalWrite(leds[i], 0);
  }
}

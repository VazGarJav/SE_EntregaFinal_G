int leds[8] = { 6, 7, 8, 9, 10, 11, 12, 13};
void setup() {
  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(10);
}
int v, k, residuo;
void loop() {
  if (Serial.available() > 0) {
    v = Serial.readString().toInt();
    while (v >= 3)
    {
      k = 7;
      int aux = v;
      while (aux > 0)
      {
        residuo = aux % 2;
        aux = aux / 2;
        digitalWrite(leds[k], residuo);
        k--;
      }
      for (; k >= 0; k--)
      {
        digitalWrite(leds[k], 0);
      }
      v = v / 2;
      delay(1000);
    }
  }
  delay(100);
}

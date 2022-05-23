int leds[8] = { 6, 7, 8, 9, 10, 11, 12, 13};
void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(10);
}
int v; //numero decimal a leer
int k;
int residuo;
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    v = Serial.readString().toInt();
    k = 7;
    while (v > 0)
    {
      residuo = v % 2;
      v = v / 2;
      digitalWrite(leds[k], residuo);
      k--;
    }
    for (; k >= 0; k--)
    {
      digitalWrite(leds[k], 0);
    }
  }
  delay(100);
}

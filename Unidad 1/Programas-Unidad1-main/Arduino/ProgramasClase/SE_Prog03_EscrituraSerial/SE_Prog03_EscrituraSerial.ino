int leds[8] = { 6, 7, 8, 9, 10, 11, 12, 13};


void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(250);
}
int v;
void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Conexion realizada");
  delay(250);
}

void limpiar()
{
  for (int i = 0; i < 8; i++)
  {
    digitalWrite(leds[i], 0);
  }
}

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
int i = 0;
String valor; //numero decimal a leer
void loop() {
  // put your main code here, to run repeatedly:
  valor = "";
  if (Serial.available() > 0)
  {
    valor = Serial.readString();
    Serial.println(valor);
    if (valor != "")
    {
      for (i = 0; i < 8; i++)
      {
        digitalWrite(leds[i], (valor.charAt(i) - 48));
      }
    }
  }
  delay(1000);
}

void limpiar()
{
  for (int i = 0; i < 8; i++)
  {
    digitalWrite(leds[i], 0);
  }
}

int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
long salida;
int sonido = A0;
int i;

void setup()
{
  for (i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);
}
String valor;
int v;
int estado = 0;
void loop()
{
  switch (estado)
  {
    case 0:
      Serial.println("Gire el potenciometro");
      estado++;
      break;
    case 1:
      salida = map(analogRead(sonido), 0, 1023, 0, 8);
      estado++;
      break;
    case 2:
      for (i = 0; i <salida; i++)
      {
        digitalWrite(leds[i], 1);
      }
      estado++;
      break;
    case 3:
      for (i = salida; i < 8; i++)
      {
        digitalWrite(leds[i], 0);
      }
      estado = 1; // ya que la lectura será infinita
      break;
  }
  delay(100);
}

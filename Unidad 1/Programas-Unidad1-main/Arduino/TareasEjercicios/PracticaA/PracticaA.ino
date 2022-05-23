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
String valor; //numero decimal a leer
int k,i,residuo,ascii;
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    valor = Serial.readString();
    
    for(i=0; i < valor.length(); i++)
    {
      k=7;
      ascii=valor.charAt(i);
      Serial.println(ascii);
      while (ascii > 0)
      {
        residuo = ascii % 2;
        ascii = ascii / 2;
        digitalWrite(leds[k], residuo);
        k--;
      }
      for (; k >= 0; k--)
      {
        digitalWrite(leds[k], 0);
      }
      delay(5000);
      limpiar();
      delay(2000);
    }
  }

}
void limpiar()
{
  for (int i = 0; i < 8; i++)
  {
    digitalWrite(leds[i], 0);
  }
}

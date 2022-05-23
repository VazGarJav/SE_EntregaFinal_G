int pulsadores[5] = { 9, 10,11, 12, 13};
int leds[5] = {2, 3, 4, 5, 6};
int i;
void setup() {
  // put your setup code here, to run once:
  for (i = 0; i < 5; i++)
  {
    pinMode(pulsadores[i], INPUT_PULLUP);
  }
  for (i = 0; i < 5; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
}
int valores[5] = {1, 1, 1, 1, 1};
String datos = "";
void loop() {
  datos = "";
  valores[0] = digitalRead(pulsadores[0]);
  valores[1] = digitalRead(pulsadores[1]);
  valores[2] = digitalRead(pulsadores[2]);
  valores[3] = digitalRead(pulsadores[3]);
  valores[4] = digitalRead(pulsadores[4]);
  for (i = 0; i < 5; i++)
  {
    datos += String(valores[i]) + " ";
  }
  Serial.println(datos);
  int indexPresionado = -1;
  for (i = 0; i < 5; i++)
  {
    if (valores[i] == 0)
      indexPresionado = i;
  }
  switch (indexPresionado)
  {
    case 0: digitalWrite(leds[0],1);
      break;
    case 1: digitalWrite(leds[1],1);
      break;
    case 2: digitalWrite(leds[2],1);
      break;
    case 3: digitalWrite(leds[3],1);
      break;
    case 4: digitalWrite(leds[4],1);
      break;
  }
  limpiar();
  delay(1000);
  for(i=0; i<5; i++)
  {
    valores[i]=1;
  }
}
void limpiar()
{
  for(i=0; i<5; i++)
  {
    digitalWrite(leds[i],0);
  }
}

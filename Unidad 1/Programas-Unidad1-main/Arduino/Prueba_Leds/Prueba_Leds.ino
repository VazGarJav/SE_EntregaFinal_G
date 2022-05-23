int leds[8] = { 6, 7, 8, 9, 10, 11, 12, 13};
int estados[8] = { 0, 0, 0, 0, 0, 0, 0, 0};
int aux[3] = {0, 0, 0};

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  randomSeed(analogRead(A0));
}
int v = -1;
int cont = 0;
void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<8; i++)
  {
    digitalWrite(leds[i],1);
    delay(1000);
  }

  for(int i=0; i<8; i++)
  {
    digitalWrite(leds[i],0);
    delay(1000);
  } 
}

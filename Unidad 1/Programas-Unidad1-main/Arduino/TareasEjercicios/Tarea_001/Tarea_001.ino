int leds[8] = { 6, 7, 8, 9, 10, 11, 12, 13};
int estados[8] = { 0, 0, 0, 0, 0, 0, 0, 0};
int aux[3] = {0, 0, 0};

void setup() {

  for (int i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  randomSeed(analogRead(A0));
}
int v = -1;
int cont = 0;
void loop() {
  do
  {
    v = random(8);
  } while (estados[v] == 1);
  aux[cont] = v;
  estados[v] = 1;
  cont++;
  if (cont > 3)
  {
    digitalWrite(leds[aux[(cont - 1) % 3]], 0);
    estados[aux[(cont - 1) % 3]] = 0;
    aux[(cont - 1) % 3] = v;
  }
  digitalWrite(leds[v], 1);
  delay(1000);
}

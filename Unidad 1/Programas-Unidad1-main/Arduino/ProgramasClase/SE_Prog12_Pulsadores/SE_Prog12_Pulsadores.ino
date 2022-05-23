int pulsador = 12;
int vpulsador=0;
void setup() {
  // put your setup code here, to run once:
  pinMode(pulsador, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  vpulsador=digitalRead(pulsador);
  Serial.println(String(vpulsador));
  delay(1000);
}

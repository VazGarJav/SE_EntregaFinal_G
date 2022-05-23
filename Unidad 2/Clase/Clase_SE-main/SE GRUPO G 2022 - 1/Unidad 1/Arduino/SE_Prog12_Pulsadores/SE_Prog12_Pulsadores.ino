int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};

int pulsador  = 2;
int sw = 3;

void setup() {
  pinMode(pulsador, INPUT_PULLUP);
  pinMode(sw, INPUT_PULLUP);
  
  // put your setup code here, to run once:
  for (int i  = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
}

int vPulsador, vSW;
void loop() {

  vPulsador = digitalRead(pulsador);
  vSW = digitalRead(sw);
  
  Serial.println("Pulsador: " +String(vPulsador) + " Switch: "+ String(vSW));
  
  delay(100);

}

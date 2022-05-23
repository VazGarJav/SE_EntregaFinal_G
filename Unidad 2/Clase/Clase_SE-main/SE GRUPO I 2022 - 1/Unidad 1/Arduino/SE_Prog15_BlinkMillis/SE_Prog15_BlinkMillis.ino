int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};

void setup() {
  // put your setup code here, to run once:
  for (int i  = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
}

long tiempoActual;
long tiempoCambioAnterior = 0;

boolean estadoLED = false;
void loop() {

  tiempoActual = millis();

  if (tiempoActual - tiempoCambioAnterior >= 1000) {
    estadoLED = !estadoLED; 
    digitalWrite(10, estadoLED);
    tiempoCambioAnterior = tiempoActual;
  }



}

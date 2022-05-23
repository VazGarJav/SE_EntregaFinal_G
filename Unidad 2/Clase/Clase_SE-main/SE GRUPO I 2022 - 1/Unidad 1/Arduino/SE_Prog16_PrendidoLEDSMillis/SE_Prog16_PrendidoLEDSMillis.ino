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

int contador = 0;
void loop() {

  tiempoActual = millis();

  if (tiempoActual - tiempoCambioAnterior >= 1000) {

    for (int i = 0; i < 8; i++) {
      digitalWrite(leds[i], 0);
    }

    estadoLED = !estadoLED;
    digitalWrite(leds[contador], estadoLED);
    tiempoCambioAnterior = tiempoActual;
     if ( estadoLED ) {
    contador++;
  }
  }


  if (contador == 8) {
    contador = 0;
  }
 




}

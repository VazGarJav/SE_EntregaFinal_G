int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};

void setup() {
  // put your setup code here, to run once:
  for (int i  = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
}

int v, vNueva;
void loop() {
  // put your main code here, to run repeatedly:
  //10bits de resolucion, 5v de referencia, ADC = > 0 - 1023

  v = analogRead(A0);

  vNueva = map(v, 0, 1023, 0, 7); //permite pasar de un intervalo origen a un intervalo destino 
  // v = variable a cambiar de intervalo
  // 0 = lim inf del intervalo origen
  // 1023 = lim sup del intervalo origen
  // 0 = lim inf del intervalo destino 
  // 7 = lim sup del intervalo destino

  Serial.println("v: " +String(v) + "vNueva: " + String(vNueva));

  for(int i = 0; i<=7; i++){
      digitalWrite(leds[i], 0);
    }
  digitalWrite(leds[vNueva],1);
  
  delay(100);

}

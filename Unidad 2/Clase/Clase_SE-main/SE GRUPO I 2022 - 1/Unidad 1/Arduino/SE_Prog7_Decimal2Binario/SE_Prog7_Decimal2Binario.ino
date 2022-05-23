int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
//bit menos significativo = 13
//bit más significativo   = 6

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);
}

int cociente; //num decimal a leer
int residuo;
int k = 7;
void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    cociente = Serial.readString().toInt();

    ///convertir v en binario para conocer los leds que se deberán prender
    k=7;
    while (cociente>0) {      
      residuo = cociente%2;
      digitalWrite(leds[k--], residuo);
      cociente = cociente/2;
    }
    //apgar los leds que no se estan utilizando para representar al numero en binario
    for(;k>=0;k--){ //for(k=?;k>=0;k--)//Version de for que no modifica la variable de inicio
        digitalWrite(leds[k], 0);
      }
    
  }
  delay(100);

}

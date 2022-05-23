int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};



String cadena;



void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }



  Serial.begin(9600);
  Serial.setTimeout(10);



  cadena = "";
}



char v[8];
//"AxxxxxxxxG" donde x = {0, 1}
//A11100110G
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    cadena += Serial.readString();



    //Opciones:
    // 1 = cadena completa COMPLETO
    // 2 = varias cadenas completas COMPLETO
    // 3 = cadena incompleta
    // 3.1 = recibir la parte que acompleta a la cadena incompleta
    // 3.2 = recibid una cadena incompleta de inicio junto con una cadena completa despues
    // 4 = cadena completa y la parte final es una cadena incompleta




    int ultimaVezDeA = cadena.lastIndexOf("A");// -1 cuando no lo encuentra
    int ultimaVezDeG = cadena.lastIndexOf("G");// -1 cuando no lo encuentra



    String subCadena = cadena.substring(ultimaVezDeA + 1, ultimaVezDeG);



    Serial.println(subCadena);



    subCadena.toCharArray(v, 8 + 1);
    aplicarSubCadena();



  }



  //PROCESO 2



  //PROCESO 3...



  //PROCESO N



  delay(100);



}



void aplicarSubCadena() {
  String vValor;
  for (int i = 0; i < 8; i++) {
    vValor = String(v[i]);
    Serial.println("It: " + String(i) + " V: " + vValor);
    digitalWrite(leds[i], v[i] - 48);
    //digitalWrite(leds[i], vValor.toInt());
  }
}

int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};

int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}



String valor;
int v;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
      Serial.println("Ingresa un numero");
      estado = 1;
      break;
    case 1:
    case 6:
      if (Serial.available() > 0) {
        valor = Serial.readString();
        if (estado == 1) {
          estado = 2;
        }
        else {
          estado = 7;
        }
      }
      break;
    case 2:
    case 7:
      if (!valor.equals("")) { //checamos si v no esta vacio .. si no estaa vacio entonces:
        v = valor.toInt();
        Serial.println(v);
        if (estado == 2) { //si se cuenta con el numero para elevar al cuadrado
          estado = 3;
        }
        else {
          //con el valor leido, necesito comprobar la respuesta del usuario:
          if (v == 1) {
            estado = 0;
          }
          else {
            estado = 5;
          }
        }
      }
      else { //Si v esta vacio, entonces necesita volver a la fase en la que lee
        //esto para obtener un valor nuevo
        estado -= 1;
      }
      break;
    case 3:
      v = v * v;
      estado = 4;
      break;
    case 4:
      Serial.println("Resultado: " + String(v));
      estado = 5;
      break;
    case 5:
      Serial.println("Deseas Repetir el algoritmo? (1 = SI / 0 = NO)");
      estado = 6 ;
      break;
  }
  delay(100);
}

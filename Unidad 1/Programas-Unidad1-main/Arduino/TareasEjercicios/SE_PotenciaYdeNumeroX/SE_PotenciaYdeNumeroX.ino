String num, pot;
double result;
int edo;
void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(100);
  edo=0;
}

void loop() {
  switch (edo) {
    case 0:
      Serial.println("Introduzca el numero que se quiere elevar: ");
      edo = 1;
      break;
    case 1:
      if (Serial.available() > 0) {
        num = Serial.readString();
        edo = 2;
      }
      break;
    case 2:
      if (num != "\n")
      {
        edo = 3;
        Serial.print(num);
      }
      else {
        edo = 1;
      }
      break;
    case 3:
      Serial.println("Introduzca potencia: ");
      edo = 4;
      break;
    case 4:
      if (Serial.available() > 0) {
        pot = Serial.readString();
        edo = 5;
      }
      break;
    case 5:
      if (pot != "\n")
      {
        edo = 6;
        Serial.print(pot);
      }
      else {
        edo = 4;
      }
      break;
    case 6:
      result = pow(num.toInt(), pot.toInt());
      edo = 7;
      break;
    case 7:
      Serial.println("Su resultado es: " + String(result));
      edo = 8;
      break;
    case 8:
      Serial.println("Volver a repetirlo? (1 = SÍ / 0 = NO)");
      edo = 9;
      break;
    case 9:
      if (Serial.available() > 0) {
        num = Serial.readString();
        edo = 10;
      }
      break;
    case 10:
      if (num != "\n")
      {
        edo = 11;
      }
      else {
        edo = 9;
      }
      break;
    case 11:
      if(num.toInt() == 1)
      {
        edo = 0;
      }else
      {
        Serial.println("Bye");
        edo = 12;
      }
      break;
  }

  delay(100);
}

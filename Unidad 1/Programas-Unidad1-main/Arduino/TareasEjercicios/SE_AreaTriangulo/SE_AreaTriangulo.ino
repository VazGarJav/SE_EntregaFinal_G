float area, base, A;
String tempA, tempB;
int edo;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(250);
  edo = 0;
}
void loop() {
  switch (edo) {
    case 0:
      Serial.print("Base: ");
      edo++;
      break;
    case 1:
      if (Serial.available() > 0) {
        tempB = Serial.readString();
        base = tempB.toFloat();
        Serial.println(String(base));
        edo++;
      }
      break;
    case 2:
      Serial.print("Altura: ");
      edo++;
      break;
    case 3:
      if (Serial.available() > 0) {
        tempA = Serial.readString();
        A = tempA.toFloat();
        edo++;
        Serial.println(String(A));
      }
      break;
    case 4:
      area = (base * A)/2;
      edo++;
      break;
    case 5:
      Serial.println("El area del Triangulo es : " + String(area));
      edo++;
      break;
    case 6:
      edo = 0;
      break;
  }
  delay(100);
}

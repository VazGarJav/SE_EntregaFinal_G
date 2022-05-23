int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}
String valor;
int v, tabla, respuesta, aciertos = 0, cont = 1;
void loop() {
  switch (estado) {
    case 0:
    case 3:
      if (estado == 0)
      {
        Serial.println("La tabla es de que numero ?");
      }
      else
      {
        if (estado == 3)
        {
          Serial.println("Cuanto es " + String(tabla) + " * " + String(cont));
        }
      }
      estado++;
    case 1:
    case 4:
    case 8:
      if (Serial.available() > 0)
      {
        valor = Serial.readString();
        estado++;
      }
      break;
    case 2:
    case 5:
    case 9:
      if (!valor.equals(""))
      {
        v = valor.toInt();
        Serial.print(valor);
        if (estado == 2)
        {
          Serial.print("\n");
          tabla = v;
          estado++;
        }
        else
        {
          if (estado == 5)
          {
            if (cont <= 10)
            {
              if (v == (tabla * cont))
              {
                Serial.println("✓\n");
                aciertos++;
              }
              else
              {
                Serial.println("X\n");
              }
              cont++;
              estado = 3;
            }
            if(cont==11)
            {
              estado = 6;
            }
          }
          else
          {
            if (v == 1)
            {
              estado = 0;
              aciertos = 0;
              cont = 1;
            }
            else
            {
              estado = 7;
            }
          }
        }
      }
      break;
    case 6:
      Serial.println("Usted obtuvo " + String(aciertos) + " aciertos!\n");
      estado++;
      break;
    case 7:
      Serial.println("Desea repetir el algoritmo 1=SI / 0= NO");
      estado++;
      break;
  }
  delay(100);
}

int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};

int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}
String valor;
int res[8];
int res2[8];
int v;
int t1, t2;
int cont = 1;
int serie1 = 0, serie2 = 0;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
    case 3:
      if (estado == 0)
      {
        Serial.println("Ingrese el primer termino");

      }
      else
      {
        if (estado == 3)
        {
          Serial.println("Ingrese el segundo termino");
        }
      }
      estado++;
      break;
    case 1:
    case 4:
    case 10:
      if (Serial.available() > 0)
      {
        valor = Serial.readString();
        Serial.println(valor);
        estado++;
      }
      break;
    case 2:
    case 5:
    case 11:
      if (!valor.equals(""))
      {
        v = valor.toInt();
        if (estado == 2)
        {
          t1 = v;
          estado++;
        }
        else
        {
          if (estado == 5)
          {
            t2 = v;
            estado++;
          }
          else
          {
            if (v == 1)
            {
              estado = 0;
            }
            else
            {
              estado = 9;
            }
          }
        }
      }

      break;

    case 6:
      Serial.println("");
      serie1 = t1 * cont;
      Serial.println("Serie 1: " + String(serie1));
      estado++;
      break;
    case 7:
      serie2 = t2 * cont;
      Serial.println("Serie 2: " + String(serie2));
      estado++;
      break;
    case 8:
      if (cont < 10)
      {
        estado = 6;
        cont++;
      }
      else
      {
        estado = 9;
        cont = 1;
      }
      break;
    case 9:
      Serial.println("Desea repetir el algoritmo? 1=SI, 0=NO");
      estado = 10;
      break;
  }
  delay(100);
}

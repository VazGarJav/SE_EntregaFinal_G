int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}
String valor;
float v;
float x1, y1, x2, y2;
float distancia;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
    case 3:
    case 6:
    case 9:
      if (estado == 0)
      {
        Serial.println("Ingrese el valor de x1");
      }
      else
      {
        if (estado == 3)
        {
          Serial.println("Ingrese el valor de y1");
        }
        else
        {
          if (estado == 6)
          {
            Serial.println("Ingrese el valor de x2");
          }
          else
          {
            Serial.println("Ingrese el valor de y2");
          }
        }
      }
      estado++;
      break;
    case 1:
    case 4:
    case 7:
    case 10:
    case 15:
      if (Serial.available() > 0)
      {
        valor = Serial.readString();
        estado++;
      }
      break;
    case 2:
    case 5:
    case 8:
    case 11:
    case 16:
      if (!valor.equals(""))
      {
        Serial.println(valor);
        v = valor.toFloat();
        if (estado == 2)
        {
          x1 = v;
          estado++;
        }
        else
        {
          if (estado == 5)
          {
            y1 = v;
            estado++;
          }
          else
          {
            if (estado == 8)
            {
              x2 = v;
              estado++;
            }
            else
            {
              if (estado == 11)
              {
                y2 = v;
                estado++;
              }
              else
              {
                if (v == 1)
                {
                  estado = 0;
                }
                else
                  estado = 14;
              }
            }
          }
        }
      }
      break;
    case 12:
      distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
      estado++;
      break;
    case 13:
      Serial.println("La distancia es: " + String (distancia));
      estado++;
      break;
    case 14:
      Serial.println("\nDesea repetir el algoritmo: 1=SI / 0= NO");
      estado++;
      break;
  }
  delay(100);
}

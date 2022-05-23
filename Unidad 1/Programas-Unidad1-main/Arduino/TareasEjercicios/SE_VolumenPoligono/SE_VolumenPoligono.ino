int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
int estado = 0;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}
String valor;
int volumen;
int v;
int ancho, largo, alto;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
    case 3:
    case 6:
      if (estado == 0)
      {
        Serial.println("Ingrese el ancho del polígono");
      }
      else
      {
        if (estado == 3)
        {
          Serial.println("Ingrese el alto del poligono");
        }
        else
        {
          Serial.println("Ingrese el largo del polígono");
        }
      }
      estado++;
      break;
    case 1:
    case 4:
    case 7:
    case 12:
      if (Serial.available() > 0)
      {
        valor = Serial.readString();
        Serial.println(valor);
        estado++;
      }
      break;
    case 2:
    case 5:
    case 8:
    case 13:
      if (!valor.equals(""))
      {
        v = valor.toInt();
        if (estado == 2)
        {
          ancho = v;
          estado++;
        }
        else
        {
          if (estado == 5)
          {
            alto = v;
            estado++;
          }
          else
          {
            if (estado == 8)
            {
              largo = v;
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
                estado = 11;
              }
            }
          }
        }
      }
      break;
    case 9:
      volumen = ancho * alto * largo;
      estado++;
      break;
    case 10:
      Serial.println("El volumen es: "+String(volumen));
      estado++;
      break;
    case 11:
      Serial.println("Desea repetir el algoritmo? 1=SI, 0=NO");
      estado = 12;
      break;
  }
  delay(100);
}

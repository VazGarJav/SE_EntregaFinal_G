int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}
String valor;
float area;
float p;
float v;
float nlados, ldelados, apotema;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
    case 3:
    case 6:
      if (estado == 0)
      {
        Serial.println("Ingrese el numero de lados");
      }
      else
      {
        if (estado == 3)
        {
          Serial.println("Ingrese la longitud de los lados");
        }
        else
        {
          Serial.println("Ingrese el apotema");
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
        v = valor.toFloat();
        if (estado == 2)
        {
          nlados = v;
          estado++;
        }
        else
        {
          if (estado == 5)
          {
            ldelados = v;
            estado++;
          }
          else
          {
            if (estado == 8)
            {
              apotema = v;
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
      p = nlados*ldelados;
      area = (p*apotema)/2;
      estado++;
      break;
    case 10:
      Serial.println("El area es: "+String(area));
      estado++;
      break;
    case 11:
      Serial.println("Desea repetir el algoritmo? 1=SI, 0=NO");
      estado = 12;
      break;
  }
  delay(100);
}
  

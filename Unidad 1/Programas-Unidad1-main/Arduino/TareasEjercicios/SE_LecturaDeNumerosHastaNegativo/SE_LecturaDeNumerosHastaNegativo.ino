int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}
String valor;
int cont = 0;
int v;
void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
      Serial.print("Ingrese un numero positivo: ");
      estado++;
      break;
    case 1:
    case 6:
      if (Serial.available() > 0)
      {
        valor = Serial.readString();
        Serial.print(valor);
        estado++;
      }
      break;
    case 2:
    case 7:
      if (!valor.equals(""))
      {
        v = valor.toInt();
        estado++;
      }
      break;
    case 3:
    case 8:
      if (estado == 3)
      {
        if (v >= 0)
        {
          estado = 0;
          cont++;
        }
        else
        {
          estado = 4;
        }
      }
      else
      {
        if (estado == 8)
        {
          if (v == 1)
          {
            estado = 0;
            cont = 0;
          }
          else
          {
            estado = 5;
          }

        }

      }
      break;
    case 4:
      Serial.println("El numeros de positivos es: " + String(cont));
      estado++;
      break;
    case 5:
      Serial.println("Desea repetir el algoritmo? 1=SI, 0=NO");
      estado = 6;
      break;
  }
  delay(100);
}

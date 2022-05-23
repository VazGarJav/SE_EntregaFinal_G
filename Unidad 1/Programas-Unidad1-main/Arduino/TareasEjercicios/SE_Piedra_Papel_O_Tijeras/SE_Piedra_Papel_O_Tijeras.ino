int estado = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

String valor;
int v;
int movida;

void loop() {
  // put your main code here, to run repeatedly:
  switch (estado) {
    case 0:
      Serial.println("Ingresa tu movida (1.Piedra/2.Papel/3.Tijeras)");
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
        if (estado == 2) {
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
    movida = random(1,3);
            v = valor.toInt();
        if(v==1)
        {
         Serial.println("TU: Piedra");
        }
         if(v==2)
        {
         Serial.println("TU: Papel");
        }
         if(v==3)
        {
         Serial.println("TU: Tijera");
        }
        
     if(movida==1)
        {
         Serial.println("CPU: Piedra");
        }
         if(movida==2)
        {
         Serial.println("CPU: Papel");
        }
         if(movida==3)
        {
         Serial.println("CPU Tijera");
        }
    Serial.println("------------------");
    
      if(movida == 1 && v ==1)
      {
     Serial.println("Resultado: EMPATE " );
     Serial.println("TU PIEDRA | CPU PIEDRA" );
      }
          if(movida == 2 && v ==2)
      {
     Serial.println("Resultado: EMPATE " );
     Serial.println("TU PAPEL | CPU PAPEL" );
      }
          if(movida == 3 && v ==3)
      {
     Serial.println("Resultado: EMPATE " );
     Serial.println("TU PIEDRA | CPU PIEDRA" );
      }
          if(movida == 1 && v ==2)
      {
     Serial.println("Resultado: GANASTE" );
     Serial.println("TU PAPEL | CPU PIEDRA" );
      }
              if(movida == 1 && v ==3)
      {
     Serial.println("Resultado: PERDISTE" );
     Serial.println("TU TIJERAS | CPU PIEDRA" );
      }
              if(movida == 2 && v ==1)
      {
     Serial.println("Resultado: PERDISTE" );
     Serial.println("TU PIEDRA | CPU PAPEL" );
      }
              if(movida == 2 && v ==3)
      {
     Serial.println("Resultado: GANASTE" );
     Serial.println("TU TIJERAS | CPU PAPEL" );
      }
              if(movida == 3 && v ==1)
      {
     Serial.println("Resultado: GANASTE" );
     Serial.println("TU PIEDRA | CPU PAPEL" );
      }
              if(movida == 3 && v ==2)
      {
     Serial.println("Resultado: PERDISTE" );
     Serial.println("TU PAPEL | CPU TIJERAS" );
      }
       
      estado = 4;
      break;
    case 4:
      estado = 5;
      break;
    case 5:
      Serial.println("Deseas Volver a Jugar? (1 = SI / 0 = NO)");
      estado = 6 ;
      break;
  }

  delay(100);
}
